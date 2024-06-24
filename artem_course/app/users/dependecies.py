from datetime import datetime, timezone

from fastapi import Depends, HTTPException, Request, status
from jose import JWTError, jwt

from app.config import settings
from app.exception import (
    IncorrectTokenFormatExeption,
    NoTokenProvidedExeption,
    NoUserWithThisIdExeption,
    TokenIsntFreshExeption,
)
from app.users.dao import UsersDAO
from app.users.models import Users


def get_token_from_request(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise NoTokenProvidedExeption
    return token


async def get_current_user(token: str = Depends(get_token_from_request)) -> Users:
    try:
        payload = jwt.decode(token, settings.HASH_KEY, settings.HASH_ALGO)
        expire: str = payload.get("exp")
        if not expire or int(expire) < datetime.now(timezone.utc).timestamp():
            raise TokenIsntFreshExeption
        user_id: str = payload.get("sub")
        if not user_id or not int(user_id):
            raise IncorrectTokenFormatExeption
        user = await UsersDAO.find_by_id(int(user_id))
        if not user:
            raise NoUserWithThisIdExeption
        return user

    except JWTError as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"JWT error:{err}"
        )
