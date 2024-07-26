from datetime import datetime

import pytest

from app.bookings.dao import BookingDAO
from app.users.dao import UsersDAO


@pytest.mark.asyncio
async def test_add_and_get_booking():
    user = await UsersDAO.find_by_id(2)
    new_booking = await BookingDAO.add(
        room_id=2,
        date_from=datetime.strptime("2023-07-10", "%Y-%m-%d"),
        date_to=datetime.strptime("2023-07-24", "%Y-%m-%d"),
        user=user,
    )

    assert new_booking.user_id == 2
    assert new_booking.room_id == 2
    assert await BookingDAO.find_by_id(new_booking.id)
    await BookingDAO.delete_by_id(new_booking.id)
    assert await BookingDAO.find_by_id(new_booking.id) is None
