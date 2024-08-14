from fastapi import APIRouter, Depends, Response, status

from app.exception import IncorectUserNameExeption, UserAlreadyExistsExeption
from app.users.auth import authenticate_user, create_access_token, hash_password
from app.users.dao import UsersDAO
from app.users.dependecies import get_current_user
from app.users.models import Users
from app.users.schemas import SUserAuth

router = APIRouter(
    prefix="/auth",
    tags=["Auth and Users"],
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user_data: SUserAuth) -> dict:
    existing_users = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_users:
        raise UserAlreadyExistsExeption

    hashed_password = hash_password(user_data.password)
    await UsersDAO.insetr_data(email=user_data.email, hashed_password=hashed_password)

    return {"status": "created"}


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth) -> dict:
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorectUserNameExeption

    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)

    return {"id": user.id, "email": user.email, "access_token": access_token}


@router.post("/logout")
async def login_logout(response: Response):
    response.delete_cookie("booking_access_token")


@router.get("/me")
async def get_user_me(current_user: Users = Depends(get_current_user)):
    return current_user