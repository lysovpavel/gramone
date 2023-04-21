from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from gramone.models import Message
from gramone.schemas.message import MessageSchema


async def get_messages(session: AsyncSession) -> Sequence[MessageSchema]:
    result = await session.execute(select(Message).limit(20))
    return result.scalars().all()
