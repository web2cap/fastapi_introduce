from datetime import date

from fastapi import APIRouter, Depends
from fastapi_versioning import version

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBookings
from app.exception import NoEntryFoundException, NoFreeRoomsOnThisDates
from app.users.fastapi_users import current_active_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)


@router.get("")
async def get_bookings(user: Users = Depends(current_active_user)) -> list[SBookings]:
    return await BookingDAO.find_all(user_id=user.id)


@router.get("/{booking_id}")
async def get_bookings_by_id(
    booking_id: int, user: Users = Depends(current_active_user)
) -> SBookings | None:
    return await BookingDAO.find_by_id(booking_id)


@router.post("")
@version(1)
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(current_active_user),
):
    booking = await BookingDAO.add(room_id, date_from, date_to, user)
    if not booking:
        raise NoFreeRoomsOnThisDates


@router.delete("/{booking_id}")
async def delete_booking(booking_id: int, user=Depends(current_active_user)) -> SBookings:
    dropped_booking = await BookingDAO.delete_by_id(booking_id)
    if not dropped_booking:
        raise NoEntryFoundException
    return SBookings.model_validate(dropped_booking)
