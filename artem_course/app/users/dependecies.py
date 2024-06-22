from datetime import datetime, timezone

from fastapi import Depends, HTTPException, Request, status
from jose import JWTError, jwt

from app.config import settings
from app.users.dao import UsersDAO
from app.users.models import Users


def unautorized_exception(detail: str):
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)


def get_token_from_request(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        unautorized_exception("No token provided")
    return token


async def get_current_user(token: str = Depends(get_token_from_request)) -> Users:
    try:
        payload = jwt.decode(token, settings.HASH_KEY, settings.HASH_ALGO)
        expire: str = payload.get("exp")
        if not expire or int(expire) < datetime.now(timezone.utc).timestamp():
            unautorized_exception("Tonet isn't fresh")
        user_id: str = payload.get("sub")
        if not user_id or not int(user_id):
            unautorized_exception("No sub with user id in token")
        user = await UsersDAO.find_by_id(int(user_id))
        if not user:
            unautorized_exception("User with provided id is not found")
        return user

    except JWTError as err:
        unautorized_exception(f"JWT Error: {err}")
