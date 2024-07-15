import shutil

from fastapi import APIRouter, UploadFile

router = APIRouter(prefix="/images", tags=["Files upload"])


@router.post("/hotels")
async def add_hotels_image(name: int, file: UploadFile):
    with open(f"app/static/images/{name}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
