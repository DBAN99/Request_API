from Model import db_class
from Model import db_connection

enginconn = db_connection.engineconn()

def table_install():
    db_class.Docter.__table__.create(bind=enginconn.engine, checkfirst=True)
    db_class.Patient.__table__.create(bind=enginconn.engine, checkfirst=True)
    db_class.Request.__table__.create(bind=enginconn.engine, checkfirst=True)