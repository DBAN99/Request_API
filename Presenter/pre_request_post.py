from datetime import datetime
from Model import db_connection
from Model import db_query
from fastapi.responses import JSONResponse

from Presenter.pre_request_another import day_change_name, expired_time

engine = db_connection.engineconn()
session = engine.sessionmaker()
commit = db_query.db_commit
close = db_query.db_close

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
        now_str = now.strftime('%Y-%m-%d %H:%M:%S')

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
            data["request_now_datetime"] = now_str
            data["expired_time"] = expired_time(add.time)
            data["expired_date"] = add.date
            pre_post_add_request(data)

            result = db_query.db_request_select(patient_name[0],doc_name["docter_name"],now_str)

        else:
            result = JSONResponse(status_code=404, content="Time Error" )

    finally:
        close()

    return result