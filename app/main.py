"""FastAPI 入口"""
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import books

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Books API", version="0.1.0")

# 注册路由
app.include_router(books.router)