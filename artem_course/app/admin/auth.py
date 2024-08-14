import contextlib

from fastapi.security import OAuth2PasswordRequestForm
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from app.config import settings
from app.users.auth import auth_backend
from app.users.manager import get_user_manager
from app.users.user_db import get_async_session, get_user_db

get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]

        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    credentials = OAuth2PasswordRequestForm(
                        username=email, password=password
                    )
                    user = await user_manager.authenticate(credentials)
                    if user and user.is_active and user.is_superuser:
                        strategy = auth_backend.get_strategy()
                        token = await strategy.write_token(user)
                        request.session.update({"admin_auth": token})
                        return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.pop("admin_auth")
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("admin_auth")
        if not token:
            return False

        strategy = auth_backend.get_strategy()
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await strategy.read_token(token, user_manager)
                    if user and user.is_active and user.is_superuser:
                        return True
        return False


authentication_backend = AdminAuth(secret_key=settings.ADMIN_SECURE_KEY)
