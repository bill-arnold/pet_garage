# pet_garage/models.py

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    customer_id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    contact_info = Column(String)
    pets = relationship('Pet', back_populates='owner')

class Pet(Base):
    __tablename__ = 'pet'
    pet_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    name = Column(String)
    age = Column(Integer)
    breed = Column(String)
    problem = Column(String)
    doctor_id = Column(Integer, ForeignKey('doctor.doctor_id'))
    owner = relationship('Customer', back_populates='pets')
    procedures = relationship('Procedure', back_populates='pet')

class Doctor(Base):
    __tablename__ = 'doctor'
    doctor_id = Column(Integer, primary_key=True)
    name = Column(String)
    speciality = Column(String)
    contact_info = Column(String)
    pets = relationship('Pet', back_populates='doctor')
    procedures = relationship('Procedure', back_populates='doctor')

class Procedure(Base):
    __tablename__ = 'procedure'
    procedure_id = Column(Integer, primary_key=True)
    procedure_name = Column(String)
    description = Column(Text)
    doctor_id = Column(Integer, ForeignKey('doctor.doctor_id'))
    pet_id = Column(Integer, ForeignKey('pet.pet_id'))
    doctor = relationship('Doctor', back_populates='procedures')
    pet = relationship('Pet', back_populates='procedures')
