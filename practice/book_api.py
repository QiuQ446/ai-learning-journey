import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

DATA_FILE = "books.json"

# ==================== 数据模型 ====================
class book(BaseModel):
    title: str       # 书名(必填)
    author: str      # 作者(必填)
    price: float      # 价格(必填)
    year: int = 2026  # 出版年份(可选，默认2026)

class UpdateBook(BaseModel):
    author: Optional[str] = None
    price: Optional[float] = None
    year: Optional[int] = None

# ==================== 数据加载/保存 ====================
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# ==================== API 接口 ====================
@app.get("/books")
def list_books():
    """列出所有书籍"""
    data = load_data()
    return {"count": len(data), "books": data}

@app.post("/books")
def create_book(book: book):
    """新增书籍"""
    data = load_data()
    if book.title in data:
        raise HTTPException(status_code=400, detail=f"书籍 '{book.title}' 已存在")
    data[book.title] = {"author": book.author, "price": book.price, "year": book.year}
    save_data(data)
    return {"message": f"书籍 {book.title} 已添加", "data": book}

@app.put("/books/{title}")
def update_book(title: str, update: UpdateBook):
    """修改书籍信息"""
    data = load_data()
    if title not in data:
        raise HTTPException(status_code=404, detail=f"书籍 '{title}' 不存在")
    if update.author is not None:
        data[title]["author"] = update.author
    if update.price is not None:
        data[title]["price"] = update.price
    if update.year is not None:
        data[title]["year"] = update.year
    save_data(data)
    return {"message": f"书籍 {title} 已更新", "data": data[title]}

@app.delete("/books/{title}")
def delete_book(title: str):
    """删除书籍"""
    data = load_data()
    if title not in data:
        raise HTTPException(status_code=404, detail=f"书籍 '{title}' 不存在")
    del data[title]
    save_data(data)
    return {"message": f"书籍 {title} 已删除"}