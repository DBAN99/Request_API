import sqlalchemy
from sqlalchemy import text
from Model import db_connection
from Model import db_class


engine = db_connection.engineconn()
session = engine.sessionmaker()
docter = db_class.Docter

# COMMIT
def db_commit():
    return session.commit()

# CLOSE
def db_close():
    return session.close()

def db_post_docter(add):
    add_docter = docter(docter_name = add.docter_name, hospital_name = add.hospital_name, department = add.department,
                        nonpaid= add.nonpaid, day_start_time = add.day_start, day_end_time= add.day_end,
                        day_start_rest_time = add.rest_start,day_end_rest_time=add.rest_end ,
                        sat_start_time = add.sat_start, sat_end_time= add.sat_end, sun_start_time=add.sun_start , sun_end_time=add.sun_end,
                        holiday = add.holiday, work_day = add.workday )
    result = session.add(add_docter)
    return result

def db_get_docter():
    sql = text("SELECT * FROM docter WHERE MATCH(docter_name, hospital_name,department) AGAINST('string');")
    result = session.execute(sql)
    # sql1 = text("ALTER TABLE docter ADD FULLTEXT(docter_name, hospital_name,department);")
    # result = session.execute(sql1)
    return result

