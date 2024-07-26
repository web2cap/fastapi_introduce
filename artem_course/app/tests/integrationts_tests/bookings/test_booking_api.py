import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "room_id, date_from, date_to, status_code",
    [
        *[(4, "2030-05-01", "2030-05-15", 200)] * 8,
        (4, "2030-05-09", "2030-05-23", 409),
        (4, "2030-05-10", "2030-05-24", 409),
    ],
)
async def test_add_and_get_booking(
    room_id,
    date_from,
    date_to,
    status_code,
    authenticated_ac: AsyncClient,
):
    response = await authenticated_ac.post(
        "/bookings",
        params={"room_id": room_id, "date_from": date_from, "date_to": date_to},
    )
    assert response.status_code == status_code
    response = await authenticated_ac.get("/bookings")


async def test_get_and_delete_bookings(authenticated_ac: AsyncClient):
    response = await authenticated_ac.get("/bookings")

    assert len(response.json()) == 10

    for booking in response.json():
        response = await authenticated_ac.delete(f"/bookings/{booking['id']}")
        assert response.status_code == 200
