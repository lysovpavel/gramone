from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import Mapped, mapped_column


from src.db.base import Base


class BaseModel(Base):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    @property
    def pk(self):
        return getattr(self, inspect(self.__class__).primary_key[0].name)

    async def before_save(self, *args, **kwargs):
        pass

    async def after_save(self, *args, **kwargs):
        pass

    async def save(self, session: AsyncSession, commit=True):
        await self.before_save()
        session.add(self)
        if commit:
            try:
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e

        await self.after_save()

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.pk}>"

    def __str__(self):
        return f"<{self.__class__.__name__} {self.pk}>"
