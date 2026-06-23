"""数据库模型"""
from sqlalchemy import Column, Integer, String
from app.database import Base

class BookDB(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    pages = Column(Integer)