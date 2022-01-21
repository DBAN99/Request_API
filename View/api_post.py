from datetime import time

from pydantic import BaseModel
from fastapi import APIRouter

from Presenter import pre_request

router = APIRouter()

class AddDocter(BaseModel):
    docter_name: str
    hospital_name: str
    department : str
    nonpaid : str
    day_start_time : time
    day_end_time : time
    day_start_rest : time
    day_end_rest : time
    sat_start_time : time
    sat_end_time : time
    sun_start_time : time
    sun_end_time : time
    holiday : str
    workday : str

class AddPatient(BaseModel):
    patient_name : str

class AddRequest(BaseModel):
    patient_id : int
    docter_id : int
    date: str
    time : str

@router.post('/docter', tags=["add"])
async def add_post_docter(add : AddDocter):
    result = pre_request.pre_post_doc(add)

    return result

@router.post('/patient', tags=["add"])
async def add_post_patient(add : AddPatient):
    result = pre_request.pre_post_patient(add)

    return result

@router.post('/request', tags=["add"])
async def add_post_request(add : AddRequest):
    result = pre_request.pre_post_request(add)

    return result
