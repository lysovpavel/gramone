import logging
from functools import wraps

from aiogram import Bot, Dispatcher, executor, types
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from config import BOT_API_TOKEN
from db.base import async_session_maker
from gramone.models import User, Chat, Message
from open_ai.service import get_answer


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot)


async def _save_message(message: types.Message):
    async with async_session_maker() as session:
        result = await session.execute(select(User).filter(User.id == message.from_user.id))
        user = result.scalars().first()
        if not user:
            user = User(id=message.from_user.id, first_name=message.from_user.first_name,
                        last_name=message.from_user.last_name, username=message.from_user.username,
                        is_bot=message.from_user.is_bot)
            await user.save(session)
        result = await session.execute(select(Chat).filter(Chat.id == message.chat.id))
        chat = result.scalars().first()
        if not chat:
            chat = Chat(id=message.chat.id, first_name=message.chat.first_name,
                        last_name=message.chat.last_name, username=message.chat.username,
                        title=message.chat.title, type=message.chat.type)
            await chat.save(session)
        reply_to_message_id = message.reply_to_message.message_id if message.reply_to_message else None
        message_db = Message(user_id=user.id, chat_id=chat.id, date=message.date, text=message.text,
                             message_id=message.message_id, reply_to_message_id=reply_to_message_id)
        await message_db.save(session)


def save_message(func):
    """Декоратор сохраняющий сообщение в базу данных"""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if message := args[0] if args else None:
            print(message)
            await _save_message(message)
        sent_message = await func(*args, **kwargs)
        if sent_message:
            await _save_message(sent_message)
        return sent_message
    return wrapper


@dp.message_handler(commands=['start', 'help'])
@save_message
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет!\nЭто чат-бот подключенный к OpenAI API. Используемая языковая модель gpt-3.5-turbo. "
                        "Для того, чтобы задать вопрос используй команду:\n/gpt вопрос")


@dp.message_handler(commands=['gpt'])
@save_message
async def gpt(message: types.Message):
    async with async_session_maker() as session:
        result = await session.execute(select(Chat).options(selectinload(Chat.modifier))
                                       .filter(Chat.id == message.chat.id))
        chat = result.scalars().first()
        modifier = chat.modifier

    question = message.text[5:]
    if modifier:
        question = f'{question} {modifier.value}'
    answer = await get_answer(question)
    return await message.reply(answer)


async def get_massages(message):
    async with async_session_maker() as session:
        result = await session.execute(select(Message).filter(Message.message_id == message.message_id))
        message_db = result.scalars().first()
        messages = await _get_massages(message_db, [], session, 5)
    print(messages)


async def _get_massages(message, messages, session, count=1):
    if not count:
        return messages
    count -= 1
    if message.reply_to_message_id:
        result = await session.execute(select(Message).filter(Message.message_id == message.reply_to_message_id))
        message_reply = result.scalars().first()
        if message_reply:
            messages = await _get_massages(message_reply, messages, session, count)
    messages.append({'role': 'user', 'content': f'{message.text}'})
    return messages


@dp.message_handler()
@save_message
async def echo(message: types.Message):
    pass
    # await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
