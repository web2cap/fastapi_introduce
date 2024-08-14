from pydantic import BaseModel


class SRooms(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str
    price: int
    quantity: int
    image_id: int
