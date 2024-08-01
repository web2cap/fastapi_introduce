from datetime import date

from fastapi import APIRouter

from app.hotels.dao import HotelsDAO
from app.hotels.schemas import SHotel, SHotelsFreeRooms

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("")
async def get_hotels() -> list[SHotel]:
    return await HotelsDAO.find_all()


@router.get("/{location}")
async def get_hotels_by_location(
    location: str,
    date_from: date,
    date_to: date,
) -> SHotelsFreeRooms | None:
    hotels = await HotelsDAO.find_by_location_free_on_date(
        search_by={"location": location}, date_from=date_from, date_to=date_to
    )
    hotels_dict = HotelsDAO.shotelsrooms_typle_to_dict(hotels)
    return SHotelsFreeRooms(hotels=hotels_dict)


@router.get("/id/{id}")
async def get_hotels_by_id(id: int) -> SHotel | None:
    return await HotelsDAO.find_by_id(id)
