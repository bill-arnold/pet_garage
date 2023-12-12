# pet_garage/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pet_garage.models import Base

DATABASE_URL = "sqlite:///./pet_garage.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
