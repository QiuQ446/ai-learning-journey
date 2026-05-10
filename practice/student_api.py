import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

DATA_FILE = "Student_Scores.json"

# ==================== 数据模型 ====================
class Student(BaseModel):
    name: str
    score: float
    grade: Optional[str] = "大一"

class UpdateStudent(BaseModel):
    score: Optional[float] = None
    grade: Optional[str] = None

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
@app.get("/students")
def list_students():
    """列出所有学生及成绩"""
    data = load_data()
    return {"count": len(data), "students": data}

@app.post("/students")
def create_student(student: Student):
    """新增学生"""
    data = load_data()
    if student.name in data:
        raise HTTPException(status_code=400, detail=f"学生 '{student.name}' 已存在")
    data[student.name] = {"score": student.score, "grade": student.grade}
    save_data(data)
    return {"message": f"学生 {student.name} 已添加", "data": student}

@app.put("/students/{name}")
def update_student(name: str, update: UpdateStudent):
    """修改学生成绩或年级"""
    data = load_data()
    if name not in data:
        raise HTTPException(status_code=404, detail=f"学生 '{name}' 不存在")
    if update.score is not None:
        data[name]["score"] = update.score
    if update.grade is not None:
        data[name]["grade"] = update.grade
    save_data(data)
    return {"message": f"学生 {name} 已更新", "data": data[name]}

@app.delete("/students/{name}")
def delete_student(name: str):
    """删除学生"""
    data = load_data()
    if name not in data:
        raise HTTPException(status_code=404, detail=f"学生 '{name}' 不存在")
    del data[name]
    save_data(data)
    return {"message": f"学生 {name} 已删除"}