from fastapi import APIRouter

from Model import db_query
from Presenter import pre_request

router = APIRouter()

# 의사 검색 (문자열)
@router.get('/find/{string}', tags=["search"])
async def get_string(string : str):
    result = pre_request.pre_get_doc(string)

    return result

@router.get('/find/{date}/{time}', tags=["search"])
async def get_string(date : str , time : str):
    result = pre_request.pre_get_doc_date(date, time)

    return result


@router.get('/qwe/{id}',tags=["search"])
async def qwe(id : int):
    result = db_query.patient_id_name(id)
    return result['patient_name']


# 의사 검색 (날짜, 시간)

# 요청

# 요청 검색 (id값)

# 요청 수락 (id값)