from fastapi import APIRouter
from Presenter import pre_request

router = APIRouter()

# 의사 검색 (문자열)
@router.get('/find/{string}', tags=["search"])
async def get_string(string : str):
    result = pre_request.pre_get_doc(string)

    return result

@router.get('/find/{date}/{hour}', tags=["search"])
async def get_string(date : str,hour : int):
    result = pre_request.pre_get_doc_date(date,hour)
    return result

@router.get('/qwe', tags=["search"])
async def get_string():
    result = pre_request.qwe()

    return result




# 의사 검색 (날짜, 시간)

# 요청

# 요청 검색 (id값)

# 요청 수락 (id값)