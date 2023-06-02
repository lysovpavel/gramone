from sqladmin import ModelAdmin

from gramone.models import Modifier


class ModifierAdmin(ModelAdmin, model=Modifier):
    column_list = ['id', 'value']
    column_searchable_list = ['id', 'value']
    column_sortable_list = ['id', 'value']
    column_details_exclude_list = ['chats']
    form_excluded_columns = ['chats']
