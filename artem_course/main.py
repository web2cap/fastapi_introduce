from datetime import date
from typing import Optional

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get("/hotels")
def get_hotels(
    location: str,
    date_from: date,
    date_to: date,
    stars: Optional[int] = Query(None, ge=1, le=5),
    has_spa: Optional[bool] = None,
) -> list[SHotel]:
    hotels = [
        {"address": "Adr", "name": "Test hotel", "stars": 5},
        {"address": "Adr", "name": "Test hotel", "stars": 5},
    ]
    return hotels


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/booking")
def add_booking(booking: SBooking):
    return booking
