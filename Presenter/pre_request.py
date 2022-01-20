from Model import db_connection
from Model import db_query
from fastapi.responses import JSONResponse

engine = db_connection.engineconn()
session = engine.sessionmaker()
commit = db_query.db_commit
close = db_query.db_close

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

def pre_get_doc():

    try:
        search = db_query.db_get_docter()

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        data = search.fetchall()

        if data == {}:
            result = JSONResponse(status_code=404, content="Data Not Found")

        else:
            result = []
            for i in range(len(data)):
                result.append(data[i]['docter_name'])

    finally:
        close()


    return result