
from pydantic import BaseModel
from fastapi import APIRouter

from Presenter import pre_request

router = APIRouter()

class AddDocter(BaseModel):
    docter_name: str
    hospital_name: str
    department : str
    nonpaid : str
    day_start : int
    day_end : int
    rest_start : int
    rest_end : int
    sat_start : int
    sat_end : int
    sun_start : int
    sun_end : int
    holiday : str
    workday : str

@router.post('/add', tags=["search"])
async def post_string(add : AddDocter):
    result = pre_request.pre_post_doc(add)

    return result