from pydantic import BaseModel


class SHotels(BaseModel):
    id: int
    name: str
    location: str
    rooms_quantity: int
    image_id: int


class SHotelsFreeRooms(SHotels):
    rooms_left: int
