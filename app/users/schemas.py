from fastapi_users import schemas
from pydantic import BaseModel, EmailStr


class SUserRead(schemas.BaseUser[int]):
    pass


class SUserCreate(BaseModel):
    email: EmailStr
    password: str


class SUserUpdate(schemas.BaseUserUpdate):
    pass
