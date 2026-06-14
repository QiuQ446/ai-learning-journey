# 学习笔记 — 2026年6月14日

> 路线：纯 Python AI 应用开发 | 阶段：FastAPI 完整 CRUD（第4天）

---

## 一、今日完成的练习

| 文件 | 内容 | GitHub |
|------|------|--------|
| `practice/my_first_server.py` | 完整 CRUD：7 个接口 | ✅ 已提交 |
| `practice/database/sql_basics.py` | SQL 基础练习（待完成） | ⬜ 待提交 |

---

## 二、完整 CRUD 接口

### 昨天的 4 个接口

| 方法 | 路径 | 功能 |
|------|------|------|
| GET | `/` | 首页 |
| GET | `/hello/{name}` | 路径参数 |
| GET | `/add?a=&b=` | 查询参数 |
| POST | `/books` | 新增书 |

### 今天新增的 3 个接口

| 方法 | 路径 | 功能 |
|------|------|------|
| GET | `/books` | 查看所有书 |
| GET | `/books/{book_id}` | 查看一本书 |
| DELETE | `/books/{book_id}` | 删除一本书 |

---

## 三、完整代码

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ===== 数据模型 =====
class Book(BaseModel):
    id: int = 0
    title: str
    author: str
    pages: int

# 内存存储（重启服务器会丢失，后面换数据库）
books = []
next_id = 1

# ===== 基础路由 =====
@app.get("/")
def home():
    return {"message": "你好！我是你写的第一个服务器！"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"greeting": f"你好，{name}！"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

# ===== CRUD =====

# CREATE —— 新增
@app.post("/books")
def create_book(book: Book):
    global next_id
    book.id = next_id
    next_id += 1
    books.append(book)
    return {"message": "添加成功", "book": book}

# READ ALL —— 查全部
@app.get("/books")
def get_books():
    return books

# READ ONE —— 查一本
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    return {"error": "书不存在"}

# DELETE —— 删除
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            deleted = books.pop(i)
            return {"message": "删除成功", "book": deleted}
    return {"error": "书不存在"}
```

---

## 四、CRUD 核心模式

### 查全部（READ ALL）

```python
@app.get("/books")
def get_books():
    return books                    # 直接返回整个列表
```

### 查一个（READ ONE）

```python
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:              # 遍历列表
        if book.id == book_id:      # 找到匹配的
            return book             # 返回它
    return {"error": "书不存在"}    # 找不到
```

### 新增（CREATE）

```python
@app.post("/books")
def create_book(book: Book):
    global next_id
    book.id = next_id               # 自动分配 id
    next_id += 1                    # id 自增
    books.append(book)              # 加入列表
    return {"message": "添加成功", "book": book}
```

### 删除（DELETE）

```python
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):   # enumerate 同时拿索引和值
        if book.id == book_id:
            deleted = books.pop(i)     # pop(i) 按索引删除
            return {"message": "删除成功", "book": deleted}
    return {"error": "书不存在"}
```

**`enumerate(books)` 拆解：**

| 循环 | `i` | `book` |
|------|-----|--------|
| 第1次 | 0 | `{id: 1, title: "老巫婆", ...}` |
| 第2次 | 1 | `{id: 2, title: "猪八戒下人间", ...}` |

`books.pop(i)` 按索引精确删除，比按值删除更安全。

---

## 五、测试流程记录

```
1. POST   /books  → 添加"猪八戒下人间"  → 200，id=2
2. GET    /books  → 查看全部             → 2本书
3. GET    /books/1 → 查看第一本          → "老巫婆"
4. DELETE /books/1 → 删除第一本          → "删除成功"
5. GET    /books  → 再次查看             → 只剩"猪八戒下人间"
```

---

## 六、当前进度

```
✅ HTTP 原理（requests 发请求）
✅ FastAPI 路由（路径参数、查询参数、请求体）
✅ 完整 CRUD（GET ALL / GET ONE / POST / DELETE）
⬜ 数据库（SQLite + SQLAlchemy）
⬜ Pydantic 深入（校验、可选字段、响应模型）
⬜ 依赖注入 + 中间件
⬜ 异步编程
⬜ 测试
⬜ 项目结构 + Docker 部署
```

---

## 七、重要认知

### 当前问题：数据在内存里

```python
books = []   # ← 服务器重启，全部清空
```

### 下一步：数据库

```python
# SQLite → 数据存在 .db 文件里，硬盘持久化
# 关了电脑，数据还在
```

---

## 八、明日计划

- [ ] `sql_basics.py` 跑通（SQLite 增删改查）
- [ ] SQLAlchemy ORM 入门
- [ ] 把 FastAPI 的 books 接口从内存换成数据库

---

*笔记生成时间：2026-06-14 | 纯Python AI应用开发路线 | 第4天*