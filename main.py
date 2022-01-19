from View import api_post
from fastapi import FastAPI
from Model import db_check

def include_router(app):
    # app.include_router(api_get.router, prefix="/news")
    app.include_router(api_post.router, prefix="/docter")


def start_application():
    app = FastAPI()
    include_router(app)
    return app

db_check.table_install()
app = start_application()
