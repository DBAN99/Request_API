
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

@router.post('/search', tags=["search"])
async def post_string():

    return