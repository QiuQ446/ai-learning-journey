from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    name: str
    score: float
    grade: str = "大一"  # 默认值，可不传

@app.get("/")
def hello():
    return {"message": "你好，邱权！FastAPI 启动成功！"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"你好，{name}！"}

@app.get("/greet")
def greet(name: str, times: int = 1):
    """查询参数示例：/greet?name=邱权&times=3"""
    greeting = f"你好，{name}！"
    return {"message": greeting * times}


@app.get("/search")
def search(keyword: str, page: int = 1, size: int = 10):
    """查询参数示例：/search?keyword=Python&page=2&size=5"""
    return {
        "keyword": keyword,
        "page": page,
        "size": size,
        "result": f"正在搜索「{keyword}」，第 {page} 页，每页 {size} 条"
    }
# 临时存储（替代数据库，重启会丢失）
fake_db = []

@app.post("/students")
def create_student(student: Student):
    """创建一个新学生记录"""
    fake_db.append(student.dict())
    return {"message": f"学生 {student.name} 已创建", "data": student}

@app.get("/students")
def list_students():
    """返回所有已创建的学生"""
    return {"count": len(fake_db), "students": fake_db}