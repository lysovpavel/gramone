from sqladmin import ModelAdmin

from gramone.models import User


class UserAdmin(ModelAdmin, model=User):
    column_list = [User.id, User.username, User.first_name, User.last_name]
