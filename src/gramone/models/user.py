from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    is_bot: Mapped[bool] = mapped_column(default=False)
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    username: Mapped[str | None]
    language_code: Mapped[str | None]
    messages: Mapped[list['Message']] = relationship(back_populates='user')

    def get_or_create(self, session):
        user = session.query(User).filter(User.id == self.id).first()
        if user:
            return user
        else:
            session.add(self)
            session.commit()
            return self
