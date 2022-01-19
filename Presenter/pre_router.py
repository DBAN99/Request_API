from fastapi import APIRouter

from View import api_post

api_router = APIRouter

api_router.include_router(api_post.router, tags=["post"])