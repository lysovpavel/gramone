from datetime import datetime

from sqlalchemy import BigInteger, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel
from .chat import Chat
from .user import User


class Message(BaseModel):
    __tablename__ = "message"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    message_id: Mapped[int] = mapped_column(BigInteger)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped[User] = relationship(back_populates='messages')
    chat_id: Mapped[int] = mapped_column(ForeignKey('chat.id'))
    chat: Mapped[Chat] = relationship(back_populates='messages')
    date: Mapped[datetime]
    text: Mapped[str] = mapped_column(Text)
    reply_to_message_id: Mapped[int | None] = mapped_column(ForeignKey('message.id'))
    reply_to_message: Mapped['Message'] = relationship('Message', back_populates='reply_messages',
                                                       remote_side=[id])
    reply_messages: Mapped[list['Message']] = relationship('Message', back_populates='reply_to_message')
