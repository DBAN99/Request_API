from sqlalchemy import text
from Model import db_connection
from Model import db_class


engine = db_connection.engineconn()
session = engine.sessionmaker()
docter = db_class.Docter
patient = db_class.Patient
request = db_class.Request



# COMMIT
def db_commit():
    return session.commit()

# CLOSE
def db_close():
    return session.close()

# -------------- POST -----------------
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

def db_post_request(time,day,doc_name):
    if day == '토요일':
        result = session.query(docter.docter_name).filter(docter.docter_name == doc_name,docter.sat_start_time <= time, docter.sat_end_time >= time).first()

    elif day == '일요일':
        result = session.query(docter.docter_name).filter(docter.docter_name == doc_name,docter.sun_start_time <= time, docter.sun_end_time >= time).first()

    else:
        result = session.query(docter.docter_name).filter(docter.docter_name == doc_name ,docter.day_start_time <= time, docter.day_end_time >= time).first()

    return result



# -------------- GET -----------------

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

def db_get_request_doc(name):
    result = session.query(request.request_id,request.patient_name,request.request_date,request.request_time).filter(request.docter_name == name , request.request_apply == 0).all()

    return result

def db_get_request_apply(id):
    result = session.query(request.request_id,request.patient_name,
                           request.request_date,request.request_time,
                           request.expired_date,request.expired_time).filter(request.request_id == id).all()
    return result

# ----------------- PATCH ------------------

def db_patch_apply(id):
    result = session.query(request).filter(request.request_id == id).update({'request_apply': 1})

    return result


# -------------- ANOTHER -----------------

def db_add_data(data):
    add = request(patient_name= data["patient_name"],docter_name=data["docter_name"],
                     request_date= data["request_date"], request_time= data["request_time"] ,
                     request_now_datetime=data["request_now_datetime"],
                  expired_date=data["expired_date"], expired_time=data["expired_time"])
    result = session.add(add)

    return result

def db_request_select(patient_name, docter_name,now_time):
    result = session.query(request.request_id,request.patient_name,
                           request.docter_name,request.request_date,request.request_time,
                           request.expired_time,request.expired_date).filter(request.patient_name == patient_name, request.docter_name == docter_name,request.request_now_datetime == now_time).all()
    return result

def docter_id_name(id):
    result = session.query(docter.docter_name).filter(docter.docter_id == id).first()

    return result

def patient_id_name(id):
    result = session.query(patient.patient_name).filter(patient.patient_id == id).first()

    return result

