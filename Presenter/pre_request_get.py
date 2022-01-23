
from Model import db_connection
from Model import db_query
from fastapi.responses import JSONResponse

from Presenter.pre_request_another import day_change_name

engine = db_connection.engineconn()
session = engine.sessionmaker()
commit = db_query.db_commit
close = db_query.db_close




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