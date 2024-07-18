from typing import List

from pydantic import BaseModel


class SHotel(BaseModel):
    id: int
    name: str
    location: str
    rooms_quantity: int
    image_id: int


class SHotelFreeRooms(SHotel):
    rooms_left: int


class SHotelsFreeRooms(BaseModel):
    hotels: List[SHotelFreeRooms]
