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
                        nonpaid= add.nonpaid, day_work_time=add.day_work_time, day_rest_time=add.day_rest_time,
                        sat_work_time=add.sat_work_time, sun_work_time=add.sun_work_time,
                        holiday = add.holiday, work_day = add.workday )
    result = session.add(add_docter)
    return result

def db_get_docter(string):
    sql = text("SELECT * FROM docter WHERE MATCH(docter_name, hospital_name,department) AGAINST('{}');".format(string))
    result = session.execute(sql)

    return result

def db_get_docter_date(date,hour):

    sql = text("SELECT * FROM docter WHERE MATCH(work_day, day_work_time,day_rest_time) AGAINST('+{} +{}');".format(hour,date))
    result = session.execute(sql)

    return result

def qwe():
    sql1 = text("ALTER TABLE docter ADD FULLTEXT(work_day, day_work_time,day_rest_time);")
    result = session.execute(sql1)
    return result