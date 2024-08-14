from fastapi_users import FastAPIUsers

from app.users.auth import auth_backend
from app.users.manager import get_user_manager
from app.users.models import Users

fastapi_users = FastAPIUsers[Users, int](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
