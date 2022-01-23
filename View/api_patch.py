from pydantic import BaseModel
from fastapi import APIRouter

from Presenter import pre_request_patch

router = APIRouter()

class ApplyRequest(BaseModel):
    apply : bool


# 진료 수락
@router.patch('/apply/{request_id}', tags=["Apply"])
async def get_string(request_id : int):
    result = pre_request_patch.pre_patch_apply(request_id)

    return result