from fastapi import APIRouter, HTTPException

from app.users.auth import hash_password
from app.users.dao import UsersDAO
from app.users.schemas import SUserRegister

router = APIRouter(
    prefix="/auth",
    tags=["Auth and Users"],
)


@router.post("/register")
async def register_user(user_data: SUserRegister) -> dict:
    existing_users = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_users:
        raise HTTPException(status_code=409, detail="This email is already registered")

    hashed_password = hash_password(user_data.password)
    await UsersDAO.insetr_data(email=user_data.email, hashed_password=hashed_password)

    return {"status": "created"}
