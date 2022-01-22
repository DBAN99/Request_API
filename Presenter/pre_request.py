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
# -------------------- GET ------------------
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

def pre_get_request_serch(id):

    try:
        doc_name = db_query.docter_id_name(id)
        result = db_query.db_get_request_doc(doc_name[0])

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        if result == []:
            result = JSONResponse(status_code=404, content="Data Not Found")

    finally:
        close()

    return result

# -------------------- POST -------------------

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

def pre_post_add_request(add):

    try:
        db_query.db_add_data(add)
        commit()

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        result = JSONResponse(status_code=200, content="OK")

    finally:
        session.close()

    return result

def pre_expired_date(day,name):
    if day == '토요일':
        result = db_query.db_get_docter_time(name)
        # 토요일 시간 비교 후 해당 시간 안에 있다면 데이트 타임 +15 추가
        # 없다면 workday에 존재하는 날 중 가장 빠른 날과 시간에 +15 추가
    elif day == '일요일':
        result = db_query.db_get_docter_time(name)
        # 일요일 시간 비교 후 해당 시간 안에 있다면 데이트 타임 +15 추가
        # 없다면 workday에 존재하는 날 중 가장 빠른 날과 시간에 +15 추가

    else:
        result = db_query.db_get_docter_time(name)


def pre_post_request(add):
    try:
        data = {
            "patient_name": "",
            "docter_name": "",
            "request_date": "",
            "request_time": "",
            "request_now_datetime": ""
        }
        now = datetime.now()
        time = now.strftime('%Y-%m-%d %H:%M:%S')

        doc_name = db_query.docter_id_name(add.docter_id)
        patient_name = db_query.patient_id_name(add.patient_id)

        day = day_change_name(add.date)
        result = db_query.db_post_request(add.time, day, doc_name[0])


    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        if result == {}:
            result = JSONResponse(status_code=404, content="Data Not Found")

        elif result == doc_name:
            data["docter_name"] = doc_name["docter_name"]
            data["patient_name"] = patient_name[0]
            data["request_date"] = add.date
            data["request_time"] = add.time
            data["request_now_datetime"] = time
            pre_post_add_request(data)
            result = db_query.db_request_select(patient_name[0],doc_name["docter_name"],time)
        else:
            result = JSONResponse(status_code=404, content="Not Found" )

    finally:
        close()

    return result
