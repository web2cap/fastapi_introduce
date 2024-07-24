from datetime import date

from pydantic import BaseModel, ConfigDict


class SBookings(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int

    model_config = ConfigDict(orm_mode=True, from_attributes=True)
