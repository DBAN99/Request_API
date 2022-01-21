from datetime import datetime

from Model import db_connection
from Model import db_query
from fastapi.responses import JSONResponse

engine = db_connection.engineconn()
session = engine.sessionmaker()
commit = db_query.db_commit
close = db_query.db_close

def day_change_name(date):
    dateDict = {0: '월요일', 1: '화요일', 2: '수요일', 3: '목요일', 4: '금요일', 5: '토요일', 6: '일요일'}
    datetime_date = datetime.strptime(date, '%Y-%m-%d')
    day = dateDict[datetime_date.weekday()]
    return day


def pre_get_doc(string):

    try:
        search = db_query.db_get_docter(string)

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        data = search.fetchall()

        if data == []:
            result = JSONResponse(status_code=404, content="Data Not Found")

        else:
            result = []
            for i in range(len(data)):
                result.append(data[i]['docter_name'])

    finally:
        close()


    return result

def pre_get_doc_date(date,hour):

    try:
        day = day_change_name(date)
        result = db_query.db_get_docter_date(day,hour)

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        if result == {}:
            result = JSONResponse(status_code=404, content="Data Not Found")

    finally:
        close()

    return result

def pre_post_patient(add):

    try:
        db_query.db_post_patient(add)
        commit()

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        result = JSONResponse(status_code=200, content="OK")

    finally:
        close()

    return result

def pre_post_doc(add):

    try:
        db_query.db_post_docter(add)
        commit()

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        result = JSONResponse(status_code=200, content="OK")

    finally:
        close()

    return result

def pre_post_request(add):

    try:
        data = {
            "patient_name" : "",
            "docter_name" : "",
            "request_date" : "",
            "request_time" : "",
            "request_now_datetime" : ""
        }
        nowdate = {"request_now_datetime" : datetime.now()}
        doc_name = db_query.docter_id_name(add.docter_id)

        day = day_change_name(add.date)
        docter_name = db_query.db_post_request(add, day,doc_name)

        data["patient_name"] = db_query.patient_id_name(add.patient_id)

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        if docter_name == {}:
            result = JSONResponse(status_code=404, content="Data Not Found")
        elif docter_name != {}:
            data["docter_name"] = docter_name
            data["request_date"] = add.date
            data["request_time"] = add.time
            data["request_now_datetime"] = nowdate

    finally:
        close()

    return result
