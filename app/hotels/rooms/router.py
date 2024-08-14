from app.hotels.rooms.dao import RoomsDAO
from app.hotels.rooms.schemas import SRooms
from app.hotels.router import router


@router.get("/{hotel_id}/rooms")
async def get_rooms_in_hotel(hotel_id: int) -> list[SRooms]:
    return await RoomsDAO.find_all(hotel_id=hotel_id)
