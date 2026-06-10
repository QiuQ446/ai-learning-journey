import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# ==================== 数据模型 ====================
class book(BaseModel):
    title: str       # 书名(必填)
    author: str      # 作者(必填)
    price: float      # 价格(必填)
    year: int = 2026  # 出版年份(可选，默认202

class UpdateBook(BaseModel):
    author: Optional[str] = None
    price: Optional[float] = None
    year: Optional[int] = None

# ==================== 数据库初始化 ====================
def get_db():
    """每次请求时获取数据库连接"""
    conn = sqlite3.connect("books.db")
    conn.row_factory = sqlite3.Row  # 让查询结果可以用字段名访问
    return conn

# 启动时自动建表
conn = sqlite3.connect("books.db")
conn.execute("""
    CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    author TEXT NOT NULL,
    price REAL NOT NULL,
    year INTEGER DEFAULT 2026
)
""")
conn.close()

# ==================== API 接口 ====================
@app.get("/books")
def list_books():
    """列出所有书籍"""
    conn = get_db()
    cursor = conn.execute("SELECT title, author, price, year FROM books")
    rows = cursor.fetchall()
    conn.close()
    # 把查询结果转成字典格式
    result = {}
    for row in rows:
        result[row["title"]] = {"author": row["author"], "price": row["price"], "year": row["year"]}
    return {"count": len(result), "books": result}

@app.post("/books")
def create_book(book: book):
    """新增书籍"""
    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO books (title, author, price,year) VALUES (?, ?, ?,?)",
            (book.title, book.author, book.price, book.year)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail=f"书籍 '{book.title}' 已存在")
    conn.close()
    return {"message": f"书籍 {book.title} 已添加", "data": book}

@app.put("/books/{title}")
def update_book(title: str, update: UpdateBook):
    """修改书籍信息"""
    conn = get_db()
    # 先查是否存在
    cursor = conn.execute("SELECT * FROM books WHERE title = ?", (title,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail=f"书籍 '{title}' 不存在")
    
    # 动态构建更新语句
    fields = []
    values = []
    if update.author is not None:
        fields.append("author = ?")
        values.append(update.author)
    if update.price is not None:
        fields.append("price = ?")
        values.append(update.price)
    if update.year is not None:
        fields.append("year = ?")
        values.append(update.year)

    if fields:
        sql = f"UPDATE books SET {', '.join(fields)} WHERE title = ?"
        values.append(title)
        conn.execute(sql, values)
        conn.commit()
    
    # 返回更新后的数据
    cursor = conn.execute("SELECT title, author, price, year FROM books WHERE title = ?", (title,))
    row = cursor.fetchone()
    conn.close()
    return {"message": f"书籍 {title} 已更新", "data": dict(row)}

@app.delete("/books/{title}")
def delete_book(title: str):
    """删除书籍"""
    conn = get_db()
    cursor = conn.execute("DELETE FROM books WHERE title = ?", (title,))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail=f"书籍 '{title}' 不存在")
    conn.commit()
    conn.close()
    return {"message": f"书籍 {title} 已删除"}