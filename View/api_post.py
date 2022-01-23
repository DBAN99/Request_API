from datetime import time

from pydantic import BaseModel
from fastapi import APIRouter

from Presenter import pre_request_post

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
    time : time




# 의사 추가
@router.post('/docter', tags=["Add"])
async def add_post_docter(add : AddDocter):
    result = pre_request_post.pre_post_doc(add)

    return result

# 환자 추가
@router.post('/patient', tags=["Add"])
async def add_post_patient(add : AddPatient):
    result = pre_request_post.pre_post_patient(add)

    return result

#진료 요청
@router.post('/request', tags=["Add"])
async def add_post_request(add : AddRequest):
    result = pre_request_post.pre_post_request(add)

    return result

