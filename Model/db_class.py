from sqlalchemy import Column, BigInteger, VARCHAR, INT, TEXT,Computed
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Docter(Base):
    __tablename__ = 'docter'
    id = Column(BigInteger,nullable=False, autoincrement=True, primary_key=True)
    docter_name = Column(VARCHAR(30) ,nullable=False)
    hospital_name = Column(VARCHAR(50), nullable=False)
    department = Column(TEXT, nullable=False)
    nonpaid = Column(TEXT, nullable=True)
    day_start_time = Column(INT, nullable=True)
    day_end_time = Column(INT, nullable=True)
    day_start_rest_time = Column(INT, nullable=True)
    day_end_rest_time = Column(INT, nullable=True)
    sat_start_time = Column(INT, nullable=True)
    sat_end_time = Column(INT, nullable=True)
    sun_start_time = Column(INT, nullable=True)
    sun_end_time = Column(INT, nullable=True)
    holiday = Column(VARCHAR(10), nullable=True)
    work_day = Column(VARCHAR(255), nullable=True)


class Patient(Base):
    __tablename__ = 'patient'
    id = Column(BigInteger,nullable=False, autoincrement=True, primary_key=True)
    patient_name = Column(VARCHAR(30) ,nullable=False)

class Request(Base):
    __tablename__ = 'request'
    request_id = Column(BigInteger,nullable=False, autoincrement=True, primary_key=True)
    patient_id = Column(BigInteger)
    docter_id = Column(BigInteger)
    request_hope_time = Column(INT)
    request_end_time = Column(VARCHAR(20))
