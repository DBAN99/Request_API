import sqlalchemy
from sqlalchemy import text
from Model import db_connection
from Model import db_class


engine = db_connection.engineconn()
session = engine.sessionmaker()
docter = db_class.Docter

sql = text("SELECT * FROM news_link WHERE MATCH(link,name,test) AGAINST('일반 메라키');")
result = session.execute(sql)

asd = result.fetchall()

print(asd)

# COMMIT
def db_commit():
    return session.commit()

# CLOSE
def db_close():
    return session.close()

def db_post_docter(adddocter):
    add = docter()


