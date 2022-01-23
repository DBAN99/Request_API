from datetime import datetime, timedelta
from Model import db_connection
from Model import db_query


engine = db_connection.engineconn()
session = engine.sessionmaker()
commit = db_query.db_commit
close = db_query.db_close


def day_change_name(date):
    dateDict = {0: '월요일', 1: '화요일', 2: '수요일', 3: '목요일', 4: '금요일', 5: '토요일', 6: '일요일'}
    datetime_date = datetime.strptime(date, '%Y-%m-%d')
    day = dateDict[datetime_date.weekday()]
    return day

def expired_time(ex_time):
    str_time = ex_time.strftime("%H:%M:%S")
    time_time = datetime.strptime(str_time, "%H:%M:%S")
    expired_time = time_time + timedelta(minutes=15)
    result = expired_time.strftime("%H:%M:%S")

    return result