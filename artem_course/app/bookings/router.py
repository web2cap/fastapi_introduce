from fastapi import APIRouter

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBookings

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)

@router.get("")
async def get_bookings() -> list[SBookings]:
    return await BookingDAO.find_all()

@router.get("/{id}")
async def get_bookings_by_id(id: int) -> SBookings | None:
    return await BookingDAO.find_by_id(id)
