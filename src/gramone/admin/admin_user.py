from sqladmin import ModelView
from fastapi.requests import Request
from gramone.models import AdminUser


class AdminUserAdmin(ModelView, model=AdminUser):
    column_list = ['id', 'username', 'is_active', 'is_superuser', 'is_verified', 'created_at']

    def is_visible(self, request: Request) -> bool:
        return True

    def is_accessible(self, request: Request) -> bool:
        return True
