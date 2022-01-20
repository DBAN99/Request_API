
from pydantic import BaseModel
from fastapi import APIRouter

from Presenter import pre_request

router = APIRouter()

class AddDocter(BaseModel):
    docter_name: str
    hospital_name: str
    department : str
    nonpaid : str
    day_work_time : str
    day_rest_time: str
    sat_work_time: str
    sun_work_time: str
    holiday : str
    workday : str

@router.post('/add', tags=["search"])
async def post_string(add : AddDocter):
    result = pre_request.pre_post_doc(add)

    return result