import pytest

from app.config import settings
from app.database import Base, async_session_maker, engine


def prepare_database():
    assert settings.MODE == "TEST"


prepare_database()
