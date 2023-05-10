import logging
from functools import wraps

from aiogram import Bot, Dispatcher, executor, types
from sqlalchemy import select

from config import BOT_API_TOKEN
from db.base import async_session_maker
from gramone.models import User, Chat, Message
from open_ai.service import get_answer


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot)


def save_message(func):
    """Декоратор сохраняющий сообщение в базу данных"""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        if message := args[0] if args else None:
            async with async_session_maker() as session:
                result = await session.execute(select(User).filter(User.id == message.from_user.id))
                user = result.scalars().first()
                if not user:
                    user = User(id=message.from_user.id, first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name, username=message.from_user.username)
                    await user.save(session)
                result = await session.execute(select(Chat).filter(Chat.id == message.chat.id))
                chat = result.scalars().first()
                if not chat:
                    chat = Chat(id=message.chat.id, first_name=message.chat.first_name,
                                last_name=message.chat.last_name, username=message.chat.username,
                                title=message.chat.title, type=message.chat.type)
                    await chat.save(session)
                message_db = Message(user_id=user.id, chat_id=chat.id, date=message.date, text=message.text,
                                     message_id=message.message_id)
                await message_db.save(session)
        return await func(*args, **kwargs)

    return wrapper


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    print(message)
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(commands=['gpt'])
async def gpt(message: types.Message):
    print(message)
    question = message.text[5:]
    if str(message.chat.id) == str(-1001962667198):
        question = f"{question} Ответь в грубой и надменной форме"
    answer = await get_answer(question)
    await message.reply(answer)


@dp.message_handler()
@save_message
async def echo(message: types.Message):
    print(message)
    # await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
