from sqlalchemy import Column, BigInteger, VARCHAR, TEXT, TIME,BOOLEAN, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Docter(Base):
    __tablename__ = 'docter'
    docter_id = Column(BigInteger,nullable=False, autoincrement=True, primary_key=True)
    docter_name = Column(VARCHAR(30) ,nullable=False)
    hospital_name = Column(VARCHAR(50), nullable=False)
    department = Column(TEXT, nullable=False)
    nonpaid = Column(TEXT, nullable=False)
    day_start_time = Column(TIME, nullable=False)
    day_end_time = Column(TIME, nullable=False)
    day_start_rest = Column(TIME, nullable=False)
    day_end_rest = Column(TIME, nullable=False)
    sat_start_time = Column(TIME, nullable=False)
    sat_end_time = Column(TIME, nullable=False)
    sun_start_time = Column(TIME, nullable=False)
    sun_end_time = Column(TIME, nullable=False)
    holiday = Column(VARCHAR(10), nullable=False)
    work_day = Column(VARCHAR(255), nullable=False)

class Patient(Base):
    __tablename__ = 'patient'
    patient_id = Column(BigInteger,nullable=False, autoincrement=True, primary_key=True)
    patient_name = Column(VARCHAR(30) ,nullable=False)

class Request(Base):
    __tablename__ = 'request'
    request_id = Column(BigInteger,nullable=False, autoincrement=True, primary_key=True)
    patient_name = Column(VARCHAR(30),nullable=False)
    docter_name = Column(VARCHAR(30), nullable=False)
    request_date = Column(VARCHAR(20), nullable=False)
    request_time = Column(TIME, nullable=False)
    request_now_datetime = Column(VARCHAR(20), nullable=False)
    request_apply = Column(BOOLEAN, default= 0, nullable=False)
    expired_date = Column(DATE, nullable=False)
    expired_time = Column(TIME, nullable=False)
