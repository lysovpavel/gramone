from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel


class Chat(BaseModel):
    __tablename__ = "chat"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    username: Mapped[str | None]
    title: Mapped[str | None]
    type: Mapped[str]
    messages: Mapped[list['Message']] = relationship(back_populates='chat')
