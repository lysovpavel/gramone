from sqladmin import ModelAdmin

from gramone.models import User


class UserAdmin(ModelAdmin, model=User):
    column_list = ['id', 'username', 'first_name', 'last_name', 'created_at']
    column_searchable_list = ['id', 'username', 'first_name', 'last_name']
    column_sortable_list = ['id', 'username', 'first_name', 'last_name', 'created_at']
    column_details_exclude_list = ['messages']
    form_excluded_columns = ['messages']
