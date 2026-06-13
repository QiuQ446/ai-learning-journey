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
    title: str
    author: str
    pages: int

# 用内存列表当数据库（重启服务器就没了，先不管）
books = []

@app.post("/books")
def create_book(book: Book):
    books.append(book)
    return {"message": "添加成功", "book": book}