from sqladmin import ModelAdmin

from gramone.models import User


class UserAdmin(ModelAdmin, model=User):
    column_list = ['id', 'username', 'first_name', 'last_name', 'created_at']
    column_searchable_list = ['id', 'username', 'first_name', 'last_name']
    column_sortable_list = ['id', 'username', 'first_name', 'last_name', 'created_at']
    column_details_list = ['id', 'is_bot', 'username', 'first_name', 'last_name', 'language_code', 'created_at']