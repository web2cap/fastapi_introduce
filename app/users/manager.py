from fastapi import Depends
from fastapi_users import BaseUserManager, IntegerIDMixin

from app.config import settings
from app.users.models import Users
from app.users.schemas import SUserCreate
from app.users.user_db import get_user_db


class UserManager(IntegerIDMixin, BaseUserManager[Users, int]):
    reset_password_token_secret = settings.HASH_KEY
    verification_token_secret = settings.HASH_KEY
    user_db_model = Users

    async def on_after_register(self, user: Users, request=None):
        print(f"User {user.email} has registered.")

    async def create(
        self, user_create: SUserCreate, safe: bool = False, request=None
    ) -> Users:
        user_dict = user_create.dict()

        user = Users(
            email=user_dict["email"],
            hashed_password=self.password_helper.hash(user_dict["password"]),
            is_active=True,
            is_superuser=False,
            is_verified=True,
        )

        self.user_db.session.add(user)
        await self.user_db.session.commit()
        await self.user_db.session.refresh(user)

        return user


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
