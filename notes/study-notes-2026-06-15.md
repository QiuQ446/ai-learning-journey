# 学习笔记 — 2026年6月15日

> 路线：纯 Python AI 应用开发 | 阶段：数据库（第5天）

---

## 一、今日完成的练习

| 文件 | 内容 | GitHub |
|------|------|--------|
| `practice/database/sql_basics.py` | SQLite 原生 SQL：建表/增删改查 | ✅ 已跑通 |
| `practice/database/orm_basics.py` | SQLAlchemy ORM：对象操作数据库 | ✅ 已跑通 |
| `practice/database/fastapi_db.py` | FastAPI + SQLAlchemy 整合，数据库持久化 | ✅ 已跑通 |

---

## 二、SQLite 原生 SQL（sql_basics.py）

### 基本操作

```python
import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# 建表
cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, score INTEGER, age INTEGER)")

# 增
cursor.execute("INSERT INTO students (name, score, age) VALUES (?, ?, ?)", ("张三", 85, 20))
conn.commit()

# 查
cursor.execute("SELECT * FROM students WHERE score >= 80")
rows = cursor.fetchall()

# 改
cursor.execute("UPDATE students SET score = 95 WHERE name = '张三'")
conn.commit()

# 删
cursor.execute("DELETE FROM students WHERE name = '王五'")
conn.commit()

conn.close()
```

### 5 条 SQL 速查

| 操作 | SQL | 含义 |
|------|-----|------|
| 建表 | `CREATE TABLE 表名 (列名 类型, ...)` | 定义表格结构 |
| 增 | `INSERT INTO 表名 VALUES (?, ?)` | 加一行数据 |
| 查 | `SELECT 列 FROM 表 WHERE 条件` | 找数据 |
| 改 | `UPDATE 表 SET 列=值 WHERE 条件` | 改数据 |
| 删 | `DELETE FROM 表 WHERE 条件` | 删数据 |

---

## 三、SQLAlchemy ORM（orm_basics.py）

### 核心概念：用 Python 对象操作数据库

**手写 SQL → ORM 对比：**

| 操作 | 手写 SQL | ORM |
|------|----------|-----|
| 建表 | `CREATE TABLE ...` | 定义 `class Student(Base)` |
| 增 | `INSERT INTO ...` | `session.add(Student(...))` |
| 查 | `SELECT * FROM ...` | `session.query(Student).all()` |
| 改 | `UPDATE ... SET ...` | `student.score = 95; session.commit()` |
| 删 | `DELETE FROM ...` | `session.delete(student); session.commit()` |

### 完整代码

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, DeclarativeBase

engine = create_engine("sqlite:///test_orm.db", echo=False)

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    score = Column(Integer)
    age = Column(Integer)

Base.metadata.create_all(engine)
session = Session(engine)

# 增
s1 = Student(name="张三", score=85, age=20)
session.add(s1)
session.commit()

# 查
students = session.query(Student).filter(Student.score >= 80).all()

# 改
zhangsan = session.query(Student).filter(Student.name == "张三").first()
zhangsan.score = 95
session.commit()

# 删
session.delete(wangwu)
session.commit()
```

---

## 四、FastAPI + SQLAlchemy 整合（fastapi_db.py）

### 这是今天最重要的文件——把内存 CRUD 升级为数据库持久化

### 三层模型

```
Pydantic 模型（请求/响应）     ORM 模型（数据库表）
BookCreate / BookOut    ←→    BookModel
```

| 层 | 类 | 用途 |
|----|-----|------|
| 请求体 | `BookCreate(BaseModel)` | 接收前端发来的 JSON |
| 响应体 | `BookOut(BaseModel)` | 返回给前端的 JSON |
| 数据库 | `BookModel(Base)` | 映射到数据库表 |

### 依赖注入（Depends）

```python
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    return db.query(BookModel).all()
```

**`Depends(get_db)` 做了什么：**
1. 请求进来 → 自动调用 `get_db()`，创建数据库会话
2. 请求处理完 → 自动关闭数据库会话
3. 你不需要手动 `session.close()`

### 完整 CRUD

```python
# CREATE
@app.post("/books", response_model=BookOut)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = BookModel(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# READ ALL
@app.get("/books", response_model=list[BookOut])
def get_books(db: Session = Depends(get_db)):
    return db.query(BookModel).all()

# READ ONE
@app.get("/books/{book_id}", response_model=BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    return db.query(BookModel).filter(BookModel.id == book_id).first()

# DELETE
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    db.delete(book)
    db.commit()
    return {"message": "删除成功"}
```

---

## 五、今日踩坑

| 问题 | 原因 | 解决 |
|------|------|------|
| `table books has no column named pages` | 旧的 `books.db` 表结构没有 `pages` 列 | 删除 `books.db`，重新启动让表重建 |
| SQLAlchemy 没装到 venv | 全局装了但 venv 没装 | `.venv\Scripts\pip install sqlalchemy` |

---

## 六、当前进度

```
✅ HTTP 原理（requests 发请求）
✅ FastAPI 路由（路径参数、查询参数、请求体）
✅ 完整 CRUD（GET/POST/DELETE）
✅ 原生 SQL（sqlite3 增删改查）
✅ SQLAlchemy ORM（对象操作数据库）
✅ FastAPI + 数据库整合（依赖注入 + 持久化）
⬜ Pydantic 深入（校验、可选字段、响应模型）
⬜ 依赖注入 + 中间件
⬜ 异步编程
⬜ 测试
⬜ 项目结构 + Docker 部署
```

---

## 七、重要认知：数据库解决了什么

```
之前：books = []          ← 内存，重启就没了
现在：books.db 文件        ← 硬盘，关了电脑数据还在
```

**重启服务器 → POST 一本书 → 重启 → GET /books → 书还在！**

---

## 八、明日计划

- [ ] Pydantic 深入：字段校验、可选字段、枚举
- [ ] 依赖注入 + 中间件
- [ ] 项目结构标准化

---

*笔记生成时间：2026-06-15 | 纯Python AI应用开发路线 | 第5天*