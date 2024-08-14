from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from app.users.auth import auth_backend
from app.users.manager import get_user_manager
from app.users.models import User
from app.users.schemas import SUserCreate, SUserRead, SUserUpdate

fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])


router = APIRouter()
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_register_router(SUserRead, SUserCreate),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(SUserRead, SUserUpdate),
    prefix="/users",
    tags=["users"],
)
