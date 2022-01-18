from fastapi import FastAPI

import datetime
app = FastAPI()
import calendar


def get_days(yyyy, mm, dd):
    days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    return days[calendar.weekday(yyyy, mm, dd)]

@app.get("/")
async def root():
    a = get_days(2022,1,16)
    return a


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
