from fastapi import APIRouter
from Presenter import pre_request_get

router = APIRouter()

# 의사 검색 (문자열)
@router.get('/{string}', tags=["Search"])
async def get_docter_string(string : str):
    result = pre_request_get.pre_get_doc(string)

    return result

@router.get('/datetime/{date}/{time}', tags=["Search"])
async def get_docter_datetime(date : str , time : str):
    result = pre_request_get.pre_get_doc_date(date, time)

    return result

@router.get('/request/{docter_id}', tags=["Search"])
async def get_string(docter_id : int):
    result = pre_request_get.pre_get_request_serch(docter_id)

    return result



# 의사 검색 (날짜, 시간)

# 요청

# 요청 검색 (id값)

# 요청 수락 (id값)