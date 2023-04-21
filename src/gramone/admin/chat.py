from sqladmin import ModelAdmin

from gramone.models import Chat


class ChatAdmin(ModelAdmin, model=Chat):
    column_list = [Chat.id, Chat.username, Chat.first_name, Chat.last_name, Chat.title, Chat.type, Chat.created_at]
