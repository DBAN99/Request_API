from View import api_post, api_get, api_patch
from fastapi import FastAPI
from Model import db_check

def include_router(app):
    app.include_router(api_get.router, prefix="/get")
    app.include_router(api_post.router, prefix="/post")
    app.include_router(api_patch.router, prefix="/patch")


def start_application():
    app = FastAPI()
    include_router(app)
    return app

db_check.table_install()
app = start_application()
