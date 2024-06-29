from datetime import date
from typing import Optional

from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel

from app.bookings.router import router as router_bookings
from app.pages.router import router as router_pages
from app.users.router import router as router_users

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_pages)


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


# class HoteslSearchArgs:
#     def __init__(
#         self,
#         location: str,
#         date_from: date,
#         date_to: date,
#         stars: Optional[int] = Query(None, ge=1, le=5),
#         has_spa: Optional[bool] = None,
#     ) -> None:
#         self.location = location
#         self.date_from = date_from
#         self.date_to = date_to
#         self.stars = stars
#         self.has_spa = has_spa
#
#
# @app.get("/hotels")
# def get_hotels(search_args: HoteslSearchArgs = Depends()):  #  -> list[SHotel]:
#     hotels = [
#         {"address": "Adr", "name": "Test hotel", "stars": 5},
#         {"address": "Adr", "name": "Test hotel", "stars": 5},
#     ]
#     return search_args


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/booking")
def add_booking(booking: SBooking):
    return booking
