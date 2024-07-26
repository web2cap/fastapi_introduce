import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("kot@pes.com", "kotopes", 201),
        ("kot@pes.com", "kotOpes", 409),
        ("noemail", "kotOpes", 422),
        ("", "kotOpes", 422),
        (None, "kotOpes", 422),
        ("pes@pes.com", None, 422),
    ],
)
@pytest.mark.asyncio
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/auth/register",
        json={"email": email, "password": password},
    )
    assert response.status_code == status_code


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("test@test.com", "test", 200),
        ("artem@example.com", "artem", 200),
        ("doestnexist@example.com", "artem", 401),
    ],
)
@pytest.mark.asyncio
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post(
        "/auth/login",
        json={
            "email": email,
            "password": password,
        },
    )
    assert response.status_code == status_code
