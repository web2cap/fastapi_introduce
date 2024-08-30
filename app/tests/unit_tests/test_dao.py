import pytest

from app.users.dao import UsersDAO


@pytest.mark.parametrize(
    "user_id, email, exists",
    [
        (1, "test@test.com", True),
        (100, None, False),
    ],
)
@pytest.mark.asyncio
async def test_find_user_bu_id(user_id, email, exists):
    user = await UsersDAO.find_by_id(user_id)

    if exists:
        assert user.email == email
        assert user.id == user_id
    else:
        assert not user
