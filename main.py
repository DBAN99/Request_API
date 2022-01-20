from View import api_post,api_get
from fastapi import FastAPI
from Model import db_check

def include_router(app):
    app.include_router(api_get.router, prefix="/search")
    app.include_router(api_post.router, prefix="/docter")


def start_application():
    app = FastAPI()
    include_router(app)
    return app

db_check.table_install()
app = start_application()
