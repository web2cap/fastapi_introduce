from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from app.database import async_session_maker
from app.users.models import User


async def get_user_db():
    async with async_session_maker() as session:
        yield SQLAlchemyUserDatabase(session, User)
