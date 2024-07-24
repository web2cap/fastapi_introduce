import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_user(ac: AsyncClient):
    response = await ac.post(
        "/auth/register",
        json={"email": "new@user.com", "password": "Passwd"},
    )
    assert response.status_code == 201
