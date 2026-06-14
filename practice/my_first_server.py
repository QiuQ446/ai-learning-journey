from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message":"你好！我是你写的第一个服务器！"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"greeting":f"你好，{name}!"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}




from pydantic import BaseModel

class Book(BaseModel):
    id: int = 0
    title: str
    author: str
    pages: int

# 用内存列表当数据库（重启服务器就没了，先不管）
books = []
next_id = 1              # 自增 id

# ===== 查全部 =====
@app.get("/books")
def get_books():
    return books

# ===== 查一本 =====
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    return {"error":"书不存在"}      #实际项目用404，先简单来

# ===== 新增（改进版） =====
@app.post("/books")
def creat_book(book:Book):
    global next_id
    book.id = next_id
    next_id += 1
    books.append(book)
    return {"message": "添加成功", "book": book}

# @app.post("/books")
# def create_book(book: Book):
#     books.append(book)                   之前的
#     return {"message": "添加成功", "book": book}

# ===== 删除=====
@app.delete("/books/{book_id}")
def delete_book(book_id:int):
    for i, book in enumerate(books):
        if book_id == book.id:
            deleted = books.pop(i)
            return{"message":"删除成功","book":deleted}
    return{"error":"书不存在"}