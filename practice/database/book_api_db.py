"""
FastAPI + SQLAlchemy 整合
让 books API 数据持久化
"""

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, DeclarativeBase

# 1. 创建 FastAPI 应用
app = FastAPI()

# 2. 连接数据库
engine = create_engine('sqlite:///books.db', echo=False)

# 3. 定义基类
class Base(DeclarativeBase):
    pass

# 4. 定义数据库模型（Book 表）
class BookDB(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    pages = Column(Integer)

# 5. 创建表
Base.metadata.create_all(engine)

# 6. Pydantic 模型（用于 API 输入输出）
class Book(BaseModel):
    title: str
    author: str
    pages: int

# ===== GET /books - 查全部 =====
@app.get("/books")
def get_books():
    session = Session(engine)
    books = session.query(BookDB).all()
    # 把数据库对象转成 Pydantic 对象返回
    result = [{"id": b.id, "title": b.title, "author": b.author, "pages": b.pages} for b in books]
    session.close()
    return result

# ===== POST /books - 新增 =====
@app.post("/books")
def create_book(book: Book):
    session = Session(engine)
    # 创建数据库对象
    new_book = BookDB(title=book.title, author=book.author, pages=book.pages)
    session.add(new_book)
    session.commit()
    # 刷新获取自增 id
    session.refresh(new_book)
    result = {"id": new_book.id, "title": new_book.title, "author": new_book.author, "pages": new_book.pages}
    session.close()
    return {"message": "添加成功", "book": result}

# ===== GET /books/{id} - 查一本 =====
@app.get("/books/{book_id}")
def get_book(book_id: int):
    session = Session(engine)
    book = session.query(BookDB).filter(BookDB.id == book_id).first()
    if book:
        result = {"id": book.id, "title": book.title, "author": book.author, "pages": book.pages}
        session.close()
        return result
    session.close()
    return {"error": "书不存在"}

# ===== DELETE /books/{id} - 删除 =====
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    session = Session(engine)
    book = session.query(BookDB).filter(BookDB.id == book_id).first()
    if book:
        session.delete(book)
        session.commit()
        result = {"id": book.id, "title": book.title, "author": book.author, "pages": book.pages}
        session.close()
        return {"message": "删除成功", "book": result}
    session.close()
    return {"error": "书不存在"}