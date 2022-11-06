from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///library.db")

Base = declarative_base()

class library(Base):
    __tablename__ = 'library'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))