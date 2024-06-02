from datetime import date
from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/hotels")
def get_hotels(
    location: str,
    date_from: date,
    date_to: date,
    stars: Optional[int] = Query(None, ge=1, le=5),
    has_spa: Optional[bool] = None,
):
    return date_from, date_to
