from sqlalchemy import delete, insert, or_, select

from app.database import async_session_maker


class BaseDAO:
    model = None

    # READ
    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_by_condensed_string(cls, serach_by: dict, **filter_by):
        async with async_session_maker() as session:
            search_filters = [
                getattr(cls.model, field).ilike(f"%{value}%") for field, value in serach_by.items()
            ]
            print(search_filters)
            query = select(cls.model).where(or_(*search_filters)).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    # CREATE
    @classmethod
    async def insetr_data(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    # DELETE
    @classmethod
    async def delete_by_id(cls, id: int):
        async with async_session_maker() as session:
            query = delete(cls.model).where(cls.model.id == id).returning(cls.model)
            result = await session.execute(query)
            await session.commit()
            return result.scalars().first()