from sqlalchemy import Column, Integer, String
from database import Base

class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True)

class Source(Base):
    __tablename__ = "source"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True)
    url = Column(String)
