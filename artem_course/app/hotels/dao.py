from datetime import date

from sqlalchemy import and_, func, or_, select
from sqlalchemy.orm import aliased

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms


class HotelsDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def find_by_location_free_on_date(
        cls, search_by: dict, date_from: date, date_to: date, **filter_by
    ):
        async with async_session_maker() as session:
            h = aliased(Hotels)
            r = aliased(Rooms)
            b = aliased(Bookings)

            search_filters = [
                getattr(h, field).ilike(f"%{value}%")
                for field, value in search_by.items()
            ]

            date_conditions = or_(
                and_(b.date_from <= date_from, b.date_to > date_from),
                and_(b.date_from < date_to, b.date_to > date_to),
                and_(b.date_from <= date_from, b.date_to >= date_to),
            )

            query = (
                select(
                    h.id,
                    h.name,
                    h.location,
                    h.rooms_quantity,
                    h.image_id,
                    (func.sum(r.quantity) - func.count(b.id)).label("rooms_left"),
                )
                .outerjoin(r, r.hotel_id == h.id)
                .outerjoin(b, and_(b.room_id == r.id, date_conditions))
                .where(and_(*search_filters))
                .group_by(h.id)
                .having(func.sum(r.quantity) - func.count(b.id) > 0)
            )

            result = await session.execute(query)
            return result.all()

    @classmethod
    def shotelsrooms_typle_to_dict(cls, hotels_typle: list):
        return [
            {
                "id": hotel[0],
                "name": hotel[1],
                "location": hotel[2],
                "rooms_quantity": hotel[3],
                "image_id": hotel[4],
                "rooms_left": hotel[5],
            }
            for hotel in hotels_typle
        ]
