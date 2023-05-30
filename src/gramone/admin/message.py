from sqladmin import ModelAdmin

from gramone.models import Message


class MessageAdmin(ModelAdmin, model=Message):
    column_list = ['message_id', 'user_id', 'chat_id', 'text', 'date']
    column_searchable_list = ['message_id', 'user_id', 'chat_id', 'text']
    column_sortable_list = ['message_id', 'user_id', 'chat_id', 'text', 'date']
    name_plural = 'Messages'
