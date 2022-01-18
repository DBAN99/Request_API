
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class AddDocter(BaseModel):
    name: str
    link: str

@router.post('/add', tags=["search"])
async def post_string(add : AddDocter):


    return