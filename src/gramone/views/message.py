from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from db.base import get_session
from gramone.schemas.message import MessageSchema
from gramone.services.message import get_messages

message_router = APIRouter()


@message_router.get("/messages", response_model=list[MessageSchema])
async def get_messages_view(session: AsyncSession = Depends(get_session)):
    messages = await get_messages(session)
    return [MessageSchema(message_id=m.message_id, user_id=m.user_id, chat_id=m.chat_id, text=m.text, date=m.date)
            for m in messages]
