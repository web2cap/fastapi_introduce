from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from sqladmin import Admin

from app.admin.views import BookingsAdmin, UserAdmin
from app.bookings.router import router as router_bookings
from app.config import settings
from app.database import engine
from app.hotels.rooms.router import router as router_rooms
from app.hotels.router import router as router_hotels
from app.images.router import router as router_images
from app.pages.router import router as router_pages
from app.users.router import router as router_users

app = FastAPI()


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")


app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_pages)
app.include_router(router_hotels)
app.include_router(router_rooms)
app.include_router(router_images)


origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


admin = Admin(app, engine)


admin.add_view(UserAdmin)
admin.add_view(BookingsAdmin)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(
        settings.REDIS_CACHE_STR, encoding="utf8", decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
