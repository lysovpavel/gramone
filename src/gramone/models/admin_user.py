from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from db.base import get_async_session
from .base_model import BaseModel


class AdminUser(SQLAlchemyBaseUserTableUUID, BaseModel):
    __tablename__ = "admin_user"

    username: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, AdminUser)
