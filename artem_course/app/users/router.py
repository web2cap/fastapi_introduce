from fastapi import APIRouter, HTTPException, Response, status

from app.users.auth import authenticate_user, create_access_token, hash_password
from app.users.dao import UsersDAO
from app.users.schemas import SUserAuth

router = APIRouter(
    prefix="/auth",
    tags=["Auth and Users"],
)


@router.post("/register")
async def register_user(user_data: SUserAuth) -> dict:
    existing_users = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This email is already registered",
        )

    hashed_password = hash_password(user_data.password)
    await UsersDAO.insetr_data(email=user_data.email, hashed_password=hashed_password)

    return {"status": "created"}


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth) -> dict:
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong email or password"
        )

    access_token = create_access_token({"sub": user.id})
    response.set_cookie("booking_access_token", access_token, httponly=True)

    return {"id": user.id, "email": user.email}
