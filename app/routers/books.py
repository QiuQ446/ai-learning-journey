"""Books 路由 —— 增删查改"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_session
from app.models import BookDB
from app.schemas import BookCreate, BookResponse

router = APIRouter(prefix="/books", tags=["books"])

# ===== 查全部 =====
@router.get("/", response_model=list[BookResponse])
def get_books(session: Session = Depends(get_session)):
    books = session.query(BookDB).all()
    return books

# ===== 新增 =====
@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, session: Session = Depends(get_session)):
    new_book = BookDB(**book.model_dump())
    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    return new_book

# ===== 查一本 =====
@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, session: Session = Depends(get_session)):
    book = session.query(BookDB).filter(BookDB.id == book_id).first()
    return book

# ===== 删除 =====
@router.delete("/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    book = session.query(BookDB).filter(BookDB.id == book_id).first()
    if book:
        session.delete(book)
        session.commit()
        return {"message": "删除成功"}
    return {"error": "书不存在"}