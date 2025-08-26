from .utils import create_temporary_file

from typing import Annotated

from fastapi import File, UploadFile, APIRouter

from backend.db.vector_db import insert_chunks

router = APIRouter(
    prefix="/files",
    tags=["files"],
    responses={404: {"description": "Not found"}},
)

@router.post("/upload")
async def upload_files(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    tmp_files = await create_temporary_file(files)
    msg = insert_chunks(tmp_files) # insert the files into the vector database
    return msg
    

