from sqladmin import ModelAdmin

from gramone.models import Chat


class ChatAdmin(ModelAdmin, model=Chat):
    column_list = ['id', 'username', 'first_name', 'last_name', 'title', 'type', 'created_at']
    column_searchable_list = ['id', 'username', 'first_name', 'last_name', 'title']
    column_sortable_list = ['id', 'username', 'first_name', 'last_name', 'title', 'type', 'created_at']
    column_details_exclude_list = ['messages']
    form_excluded_columns = ['messages']
