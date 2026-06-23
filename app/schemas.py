"""Pydantic 数据校验模型"""
from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    pages: int

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    pages: int