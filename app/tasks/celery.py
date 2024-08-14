from celery import Celery

from app.config import settings

celery = Celery(
    "tasks",
    broker=settings.REDIS_CELERY_STR,
    include=["app.tasks.tasks"],
)
