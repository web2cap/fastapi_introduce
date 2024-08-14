from datetime import datetime, timedelta, timezone

import bcrypt
from jose import jwt
from pydantic import EmailStr

from app.config import settings
from app.users.dao import UsersDAO


def hash_password(password: str) -> str:
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password=pwd_bytes, salt=salt).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    plain_password_byte_enc = plain_password.encode("utf-8")
    hashed_password_byte_enc = hashed_password.encode("utf-8")

    return bcrypt.checkpw(
        password=plain_password_byte_enc, hashed_password=hashed_password_byte_enc
    )


async def authenticate_user(email: EmailStr, password: str) -> UsersDAO | None:
    user = await UsersDAO.find_one_or_none(email=email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=5)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.HASH_KEY, settings.HASH_ALGO)
