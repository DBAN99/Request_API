
from Model import db_connection
from Model import db_query
from fastapi.responses import JSONResponse

engine = db_connection.engineconn()
session = engine.sessionmaker()
commit = db_query.db_commit
close = db_query.db_close

def pre_patch_apply(id):

    try:
        ok = db_query.db_patch_apply(id)
        commit()
    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        if ok == 0:
            result = JSONResponse(status_code=404, content="Data Not Found")

        else:
            result = db_query.db_get_request_apply(id)

    finally:
        close()

    return result