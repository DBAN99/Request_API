
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

@router.get('/search', tags=["search"])
async def post_string():

    return


# 의사 검색 (문자열)

# 의사 검색 (날짜, 시간)

# 요청

# 요청 검색 (id값)

# 요청 수락 (id값)