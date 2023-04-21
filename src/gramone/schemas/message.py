from datetime import datetime

from pydantic import BaseModel, Field


class MessageSchema(BaseModel):
    message_id: int | None
    user_id: int
    chat_id: int
    date: datetime = Field(example="2019-04-01T00:00:00")
    text: str
