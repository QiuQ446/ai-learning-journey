# 学习笔记 — 2026年6月13日

> 路线：纯 Python AI 应用开发 | 阶段：基础收尾 + FastAPI 入门（第3天）

---

## 一、今日完成的练习

| 文件 | 内容 | GitHub |
|------|------|--------|
| `practice/review/file_review.py` | 文件读写 + 异常处理 6 道题 | ✅ 已提交 |
| `practice/my_first_server.py` | FastAPI 入门：4 个接口 | ✅ 已提交 |

---

## 二、文件读写 + 异常处理

### 三个模式

| 模式 | 作用 | 注意 |
|------|------|------|
| `"r"` | 读 | 文件不存在会报错 |
| `"w"` | 覆盖写 | 每次清空文件再写 |
| `"a"` | 追加写 | 在末尾添加，不删前面的 |

### 基本模板

```python
# 读
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 覆盖写
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("内容\n")

# 追加写
with open("file.txt", "a", encoding="utf-8") as f:
    f.write("追加内容\n")
```

### 异常处理

```python
try:
    num = int(input("输入数字："))
except ValueError:
    print("不是数字！")

# 带重试的循环
while True:
    try:
        return int(input("输入数字："))
    except ValueError:
        print("请重新输入！")
```

### 常见异常

| 异常 | 何时触发 |
|------|----------|
| `ValueError` | 类型转换失败 |
| `FileNotFoundError` | 文件不存在 |
| `ZeroDivisionError` | 除以 0 |

---

## 三、FastAPI 入门——从零到搭出 API 服务器

### 安装

```bash
pip install fastapi uvicorn
```

### 启动

```bash
uvicorn practice.my_first_server:app --reload
```

`--reload`：代码改了自动重启，开发必备。

### 四种接口

| 类型 | 代码 | 数据在哪 |
|------|------|----------|
| 基础路由 | `@app.get("/")` | 固定路径 |
| 路径参数 | `@app.get("/hello/{name}")` | URL 路径里 |
| 查询参数 | `@app.get("/add")` + `def add(a: int, b: int)` | `?a=10&b=25` |
| POST 请求体 | `@app.post("/books")` + Pydantic 模型 | JSON Body |

### 完整代码

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 基础路由
@app.get("/")
def home():
    return {"message": "你好！我是你写的第一个服务器！"}

# 路径参数
@app.get("/hello/{name}")
def hello(name: str):
    return {"greeting": f"你好，{name}！"}

# 查询参数
@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

# POST + Pydantic
class Book(BaseModel):
    title: str
    author: str
    pages: int

books = []

@app.post("/books")
def create_book(book: Book):
    books.append(book)
    return {"message": "添加成功", "book": book}
```

### Pydantic 是什么

```python
class Book(BaseModel):
    title: str      # 必填，必须是字符串
    author: str     # 必填，必须是字符串
    pages: int      # 必填，必须是整数
```

Pydantic 自动校验 JSON 数据类型。如果有人发 `{"title": 123, "pages": "五百"}`，FastAPI 直接返回 422 错误，不用你手写校验代码。

### 核心理解

```
之前：你用 requests 请求别人的服务器
现在：别人（浏览器）请求你的服务器，你返回 JSON

你就是 jsonplaceholder 的角色。
```

### 两个重要 URL

| URL | 功能 |
|-----|------|
| `http://127.0.0.1:8000` | 你的 API |
| `http://127.0.0.1:8000/docs` | 自动生成的接口文档，可以直接测试 |

---

## 四、Python 后端完整路线回顾

```
✅ HTTP 原理（requests 发请求）
✅ FastAPI 路由（路径参数、查询参数、请求体）
⬜ Pydantic 深入（校验、嵌套模型）
⬜ 完整 CRUD（GET/POST/PUT/DELETE）
⬜ 数据库（SQLAlchemy + SQLite）
⬜ 依赖注入 + 中间件
⬜ 异步编程
⬜ 测试
⬜ 项目结构 + Docker 部署
```

---

## 五、基础巩固阶段总览

| 日期 | 文件 | 知识点 |
|------|------|--------|
| 6.11 | `list_review.py` | 列表操作 |
| 6.11 | `dict_review.py` | 字典嵌套 |
| 6.12 | `function_review.py` | 函数 + 闭包 |
| 6.12 | `class_review.py` | 类 + 对象 |
| 6.13 | `file_review.py` | 文件读写 + 异常处理 |
| 6.13 | `my_first_server.py` | FastAPI 入门 |

---

## 六、明日计划

- [ ] 给 `/books` 加上 GET（查看所有书）、DELETE（删除单本）
- [ ] Pydantic 深入：字段校验、可选字段、响应模型
- [ ] 完整 CRUD 实现

---

*笔记生成时间：2026-06-13 | 纯Python AI应用开发路线 | 第3天*