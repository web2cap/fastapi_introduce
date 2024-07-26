from datetime import date

from fastapi import APIRouter, Depends

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBookings
from app.exception import NoEntryFoundException, NoFreeRoomsOnThisDates
from app.users.dependecies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookings]:
    return await BookingDAO.find_all(user_id=user.id)


@router.get("/{id}")
async def get_bookings_by_id(id: int, user: Users = Depends(get_current_user)) -> SBookings | None:
    return await BookingDAO.find_by_id(id)


@router.post("")
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(room_id, date_from, date_to, user)
    if not booking:
        raise NoFreeRoomsOnThisDates


@router.delete("/{id}")
async def delete_booking(id: int, user=Depends(get_current_user)) -> SBookings:
    dropped_booking = await BookingDAO.delete_by_id(id)
    if not dropped_booking:
        raise NoEntryFoundException
    return SBookings.model_validate(dropped_booking)
