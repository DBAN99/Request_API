from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model import db_auth

sql = db_auth.app

ConnectionString=f'{sql["name"]}://{sql["user"]}:{sql["password"]}@{sql["host"]}:{sql["port"]}/{sql["db"]}'

class engineconn:

    def __init__(self):
        self.engine = create_engine(ConnectionString, pool_recycle=500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connect()
        return conn