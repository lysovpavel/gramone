from sqladmin import ModelView
from fastapi.requests import Request
from gramone.models import AdminUser


class AdminUserAdmin(ModelView, model=AdminUser):
    # column_list = [User.id, User.username, User.first_name, User.last_name]
    def is_visible(self, request: Request) -> bool:
        return True

    def is_accessible(self, request: Request) -> bool:
        return True
