
from fastapi import FastAPI

from contextlib import asynccontextmanager

from db import create_tables, delete_tables

from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("DB deleted")
    await create_tables()
    print("New DB Created")
    yield
    print("Shutting down...")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)



