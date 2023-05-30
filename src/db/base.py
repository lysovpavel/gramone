from typing import AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL, DATABASE_URL_SYNC

async_engine = create_async_engine(DATABASE_URL, echo=True)
engine = create_engine(DATABASE_URL_SYNC, echo=True)
Base = declarative_base()
async_session_maker = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
session_maker = sessionmaker(bind=engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
