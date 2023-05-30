from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel


class Modifier(BaseModel):
    __tablename__ = "modifier"

    id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[str | None]
    chats: Mapped[list['Chat']] = relationship(back_populates='modifier')

    def __str__(self):
        return self.value
