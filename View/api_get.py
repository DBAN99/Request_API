from fastapi import APIRouter
from Presenter import pre_request

router = APIRouter()

# 의사 검색 (문자열)
@router.get('/find', tags=["search"])
async def get_string():
    result = pre_request.pre_get_doc()

    return result




# 의사 검색 (날짜, 시간)

# 요청

# 요청 검색 (id값)

# 요청 수락 (id값)