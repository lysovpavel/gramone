from sqladmin import Admin
from sqlalchemy import select

from config import SECRET_KEY
from db.base import engine, async_session_maker
from gramone.admin.chat import ChatAdmin
from gramone.admin.message import MessageAdmin
from gramone.admin.user import UserAdmin
from gramone.admin.admin_user import AdminUserAdmin
from gramone.app import app


from typing import Optional
from sqladmin.authentication import AuthenticationBackend
from fastapi.requests import Request
from fastapi.responses import RedirectResponse

from gramone.models import AdminUser


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]
        async with async_session_maker() as db_session:
            print(dir(db_session))
            admin_user_stmt = await db_session.execute(select(AdminUser).where(AdminUser.username == username))
            cur_user = admin_user_stmt.scalars().first()
            if cur_user and cur_user.hashed_password == password:
                request.session.update({"token": "qwerty"})
                return True
            return False

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> Optional[RedirectResponse]:
        token = request.session.get("token")

        if not token:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        # Check the token in depth


authentication_backend = AdminAuth(secret_key=SECRET_KEY)


admin = Admin(app=app, engine=engine, authentication_backend=authentication_backend)

admin.add_view(MessageAdmin)
admin.add_view(ChatAdmin)
admin.add_view(UserAdmin)
admin.add_view(AdminUserAdmin)
