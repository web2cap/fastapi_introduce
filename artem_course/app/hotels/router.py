from fastapi import APIRouter

from app.hotels.dao import HotelsDAO
from app.hotels.models import Hotels
from app.hotels.schemas import SHotels

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("")
async def get_hotels() -> list[SHotels]:
    return await HotelsDAO.find_all()
