import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# ==================== 数据模型 ====================
class Student(BaseModel):
    name: str
    score: float
    grade: Optional[str] = "大一"

class UpdateStudent(BaseModel):
    score: Optional[float] = None
    grade: Optional[str] = None

# ==================== 数据库初始化 ====================
def get_db():
    """每次请求时获取数据库连接"""
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row  # 让查询结果可以用字段名访问
    return conn

# 启动时自动建表
conn = sqlite3.connect("students.db")
conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        score REAL NOT NULL,
        grade TEXT DEFAULT '大一'
    )
""")
conn.close()

# ==================== API 接口 ====================
@app.get("/students")
def list_students():
    """列出所有学生"""
    conn = get_db()
    cursor = conn.execute("SELECT name, score, grade FROM students")
    rows = cursor.fetchall()
    conn.close()
    # 把查询结果转成字典格式
    result = {}
    for row in rows:
        result[row["name"]] = {"score": row["score"], "grade": row["grade"]}
    return {"count": len(result), "students": result}

@app.post("/students")
def create_student(student: Student):
    """新增学生"""
    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO students (name, score, grade) VALUES (?, ?, ?)",
            (student.name, student.score, student.grade)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail=f"学生 '{student.name}' 已存在")
    conn.close()
    return {"message": f"学生 {student.name} 已添加", "data": student}

@app.put("/students/{name}")
def update_student(name: str, update: UpdateStudent):
    """修改学生成绩或年级"""
    conn = get_db()
    # 先查是否存在
    cursor = conn.execute("SELECT * FROM students WHERE name = ?", (name,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail=f"学生 '{name}' 不存在")
    
    # 动态构建更新语句
    fields = []
    values = []
    if update.score is not None:
        fields.append("score = ?")
        values.append(update.score)
    if update.grade is not None:
        fields.append("grade = ?")
        values.append(update.grade)
    
    if fields:
        sql = f"UPDATE students SET {', '.join(fields)} WHERE name = ?"
        values.append(name)
        conn.execute(sql, values)
        conn.commit()
    
    # 返回更新后的数据
    cursor = conn.execute("SELECT name, score, grade FROM students WHERE name = ?", (name,))
    row = cursor.fetchone()
    conn.close()
    return {"message": f"学生 {name} 已更新", "data": dict(row)}

@app.delete("/students/{name}")
def delete_student(name: str):
    """删除学生"""
    conn = get_db()
    cursor = conn.execute("DELETE FROM students WHERE name = ?", (name,))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail=f"学生 '{name}' 不存在")
    conn.commit()
    conn.close()
    return {"message": f"学生 {name} 已删除"}