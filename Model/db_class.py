from sqlalchemy import Column, BigInteger, VARCHAR, TEXT, TIME,BOOLEAN, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Docter(Base):
    __tablename__ = 'docter'
    docter_id = Column(BigInteger,nullable=False, autoincrement=True, primary_key=True)
    docter_name = Column(VARCHAR(30) ,nullable=False)
    hospital_name = Column(VARCHAR(50), nullable=False)
    department = Column(TEXT, nullable=False)
    nonpaid = Column(TEXT, nullable=True)
    day_start_time = Column(TIME, nullable=True)
    day_end_time = Column(TIME, nullable=True)
    day_start_rest = Column(TIME, nullable=True)
    day_end_rest = Column(TIME, nullable=True)
    sat_start_time = Column(TIME, nullable=True)
    sat_end_time = Column(TIME, nullable=True)
    sun_start_time = Column(TIME, nullable=True)
    sun_end_time = Column(TIME, nullable=True)
    holiday = Column(VARCHAR(10), nullable=True)
    work_day = Column(VARCHAR(255), nullable=True)

class Patient(Base):
    __tablename__ = 'patient'
    patient_id = Column(BigInteger,nullable=False, autoincrement=True, primary_key=True)
    patient_name = Column(VARCHAR(30) ,nullable=False)

class Request(Base):
    __tablename__ = 'request'
    request_id = Column(BigInteger,nullable=False, autoincrement=True, primary_key=True)
    patient_name = Column(VARCHAR(30))
    docter_name = Column(VARCHAR(30))
    request_date = Column(VARCHAR(20))
    request_time = Column(TIME)
    request_now_datetime = Column(VARCHAR(20))
    request_apply = Column(BOOLEAN, default= 0)
    expired_date = Column(DATE)
    expired_time = Column(TIME)
