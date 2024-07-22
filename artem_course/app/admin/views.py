from sqladmin import ModelView

from app.bookings.models import Bookings
from app.hotels.models import Hotels
from app.users.models import Users


class UserAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"


class BookingsAdmin(ModelView, model=Bookings):
    column_list = [c.name for c in Bookings.__table__.c if c.name != "user_id"] + [
        Bookings.user
    ]
    name = "Booking"
    name_plural = "Bookings"


class HotelsAdmin(ModelView, model=Hotels):
    column_list = [c.name for c in Hotels.__table__.c if c.name != "rooms_id"] + [
        Hotels.rooms
    ]
    name = "Hotel"
    name_plural = "Hotels"
    icon = "fa-solid fa-hotel"
