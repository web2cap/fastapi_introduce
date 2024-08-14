import time

import sentry_sdk
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_versioning import VersionedFastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from sqladmin import Admin

from app.admin.auth import authentication_backend
from app.admin.views import BookingsAdmin, HotelsAdmin, RoomsAdmin, UserAdmin
from app.bookings.router import router as router_bookings
from app.config import settings
from app.database import engine
from app.hotels.rooms.router import router as router_rooms
from app.hotels.router import router as router_hotels
from app.images.router import router as router_images
from app.logger import logger
from app.pages.router import router as router_pages
from app.prometheus.router import router as router_prometheus
from app.users.router import router as router_users

sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app = FastAPI()

# app.include_router(router_users)
# app.include_router(router_bookings)
# app.include_router(router_pages)
# app.include_router(router_hotels)
# app.include_router(router_rooms)
# app.include_router(router_images)
# app.include_router(router_prometheus)


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


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(
        "Request execution time", extra={"process_time": round(process_time, 4)}
    )
    return response


app = VersionedFastAPI(
    app,
    version_format="{major}",
    prefix_format="/v{major}",
)

app.mount("/static", StaticFiles(directory="app/static"), "static")

instrumentator = Instrumentator(
    should_group_status_codes=False,
    excluded_handlers=[".*admin.*", "/metrics"],
)
instrumentator.instrument(app).expose(app)

admin = Admin(app, engine, authentication_backend=authentication_backend)

# admin.add_view(UserAdmin)
# admin.add_view(BookingsAdmin)
# admin.add_view(HotelsAdmin)
# admin.add_view(RoomsAdmin)
