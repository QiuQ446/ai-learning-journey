"""
FastAPI + Depends 依赖注入
让代码更简洁优雅
"""

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, DeclarativeBase

app = FastAPI()

engine = create_engine('sqlite:///books.db', echo=False)

class Base(DeclarativeBase):
    pass

class BookDB(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    pages = Column(Integer)

Base.metadata.create_all(engine)

class Book(BaseModel):
    title: str
    author: str
    pages: int


# ===== 核心：依赖注入函数 =====
def get_session():
    """每次请求自动创建 session,用完自动关闭"""
    session = Session(engine)
    try:
        yield session        # yield 相当于 return，但函数会暂停在这里
    finally:
        session.close()      # 请求结束后自动执行

# ===== GET /books - 查全部 =====
@app.get("/books")
def get_books(session: Session = Depends(get_session)):
    books = session.query(BookDB).all()
    return [{"id": b.id, "title": b.title, "author": b.author, "pages": b.pages} for b in books]

# ===== POST /books - 新增 =====
@app.post("/books")
def create_book(book: Book, session: Session = Depends(get_session)):
    new_book = BookDB(title=book.title, author=book.author, pages=book.pages)
    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    return {"message": "添加成功", "book": {"id": new_book.id, "title": new_book.title, "author": new_book.author, "pages": new_book.pages}}

# ===== GET /books/{id} - 查一本 =====
@app.get("/books/{book_id}")
def get_book(book_id: int, session: Session = Depends(get_session)):
    book = session.query(BookDB).filter(BookDB.id == book_id).first()
    if book:
        result = {"id": book.id, "title": book.title, "author": book.author, "pages": book.pages}
        return result
    return {"error": "书不存在"}

# ===== DELETE /books/{id} - 删除 =====
@app.delete("/books/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    book = session.query(BookDB).filter(BookDB.id == book_id).first()
    if book:
        session.delete(book)
        session.commit()
        return {"message": "删除成功", "book": {"id": book.id, "title": book.title, "author": book.author, "pages": book.pages}}
    return {"error": "书不存在"}