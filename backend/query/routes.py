from fastapi import APIRouter

from .rag_engine import search_query

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

@router.get("/query")
async def query(q: str|None = None):
    # This endpoint will handle queries to the database
    return search_query(q)

