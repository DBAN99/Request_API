from Model import db_connection
from Model import db_query
from fastapi.responses import JSONResponse

engine = db_connection.engineconn()
session = engine.sessionmaker()
commit = db_query.db_commit
close  = db_query.db_close

def pre_post_doc(add):

    try:
        db_query.db_post_docter(add)
        commit()

    except:
        result = JSONResponse(status_code=400, content="URL ERROR")

    else:
        result = JSONResponse(status_code=200, content="OK")

    finally:
        session.close()

    return result