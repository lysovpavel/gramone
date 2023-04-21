from sqladmin import ModelAdmin

from gramone.models import Message


class MessageAdmin(ModelAdmin, model=Message):
    column_list = [Message.message_id, Message.user_id, Message.chat_id, Message.text, Message.date]
    name_plural = 'Messages'
    # column_details_list = [Message.message_id, Message.user_id, Message.chat_id, Message.text, Message.date]
