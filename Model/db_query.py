from sqlalchemy import text
from Model import db_connection
from Model import db_class


engine = db_connection.engineconn()
session = engine.sessionmaker()
docter = db_class.Docter
patient = db_class.Patient



# COMMIT
def db_commit():
    return session.commit()

# CLOSE
def db_close():
    return session.close()

def db_post_docter(add):
    add_docter = docter(docter_name = add.docter_name, hospital_name = add.hospital_name, department = add.department,
                        nonpaid= add.nonpaid, holiday = add.holiday, work_day = add.workday,
                        day_start_time= add.day_start_time, day_end_time= add.day_end_time,
                        day_start_rest= add.day_start_rest, day_end_rest= add.day_end_rest,
                        sat_start_time= add.sat_start_time, sat_end_time= add.sat_end_time,
                        sun_start_time= add.sun_start_time, sun_end_time= add.sun_end_time

                        )
    result = session.add(add_docter)
    return result

def db_post_patient(add):
    add_patient = patient(patient_name= add.patient_name)
    result = session.add(add_patient)
    return result

def db_get_docter(string):
    sql = text("SELECT * FROM docter WHERE MATCH(docter_name, hospital_name,department) AGAINST('{}');".format(string))
    result = session.execute(sql)

    return result

def db_get_docter_date(date,hour):
    if date == '토요일':
        result = session.query(docter.docter_name).filter(docter.sat_start_time <= hour, docter.sat_end_time >= hour).all()

    elif date == '일요일':
        result = session.query(docter.docter_name).filter(docter.sun_start_time <= hour, docter.sun_end_time >= hour).all()

    else:
        result = session.query(docter.docter_name).filter(docter.day_start_time <= hour, docter.day_end_time >= hour).all()
    return result

def db_post_request(add,day,doc_name):
    if day == '토요일':
        result = session.query(docter.docter_name).filter(docter.docter_name == doc_name,docter.sat_start_time <= add.time, docter.sat_end_time >= add.time).first()

    elif day == '일요일':
        result = session.query(docter.docter_name).filter(docter.docter_name == doc_name,docter.sun_start_time <= add.time, docter.sun_end_time >= add.time).first()

    else:
        result = session.query(docter.docter_name).filter(docter.docter_name == doc_name ,docter.day_start_time <= add.time, docter.day_end_time >= add.time).first()

    return result

def docter_id_name(id):
    result = session.query(docter.docter_name).filter(docter.docter_id == id).first()

    return result

def patient_id_name(id):
    result = session.query(patient.patient_name).filter(patient.patient_id == id).first()

    return result