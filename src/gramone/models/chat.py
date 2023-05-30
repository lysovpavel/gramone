from sqlalchemy import BigInteger, ForeignKey
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
    modifier_id: Mapped[int | None] = mapped_column(ForeignKey('modifier.id'))
    modifier: Mapped['Modifier'] = relationship(back_populates='chats')
    messages: Mapped[list['Message']] = relationship(back_populates='chat')
