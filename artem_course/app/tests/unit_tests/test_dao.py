import pytest

from app.users.dao import UsersDAO


@pytest.mark.parametrize(
    "id, email, exists",
    [
        (1, "test@test.com", True),
        (100, None, False),
    ],
)
@pytest.mark.asyncio
async def test_find_user_bu_id(id, email, exists):
    user = await UsersDAO.find_by_id(id)

    if exists:
        assert user.email == email
        assert user.id == id
    else:
        assert not user
