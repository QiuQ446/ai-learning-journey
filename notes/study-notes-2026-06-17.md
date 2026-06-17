# FastAPI + 数据库整合 — 2026年6月17日

> 路线：纯 Python AI 应用开发 | 阶段：数据库进阶（第7天）

---

## 一、今日完成的练习

| 文件 | 内容 | 状态 |
|------|------|------|
| practice/database/book_api_db.py | FastAPI + SQLAlchemy 整合，持久化 CRUD | ✅ 已跑通 |

---

## 二、核心收获

### 内存版 vs 数据库版

| 对比 | 内存版 | 数据库版 |
|------|--------|----------|
| 存储 | books = [] 列表 | books.db SQLite 文件 |
| 重启后 | 数据丢失 | 数据保留 |
| 操作方式 | 列表操作 | SQLAlchemy ORM |

### 遇到的坑

books.db 旧表缺少 pages 列 → 删除旧数据库，重新建表即可

---

## 三、核心代码结构

### 数据库模型
class BookDB(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)

### CRUD 路由

GET /books → session.query(BookDB).all()
POST /books → session.add(BookDB(...)) → commit()
GET /books/{id} → session.query(BookDB).filter(...).first()
DELETE /books/{id} → session.delete(book) → commit()

---

## 四、测试结果

POST 蜘蛛侠 → 200 ✅
POST 侏罗纪 → 200 ✅
POST 代码的逻辑 → 200 ✅
GET /books → 返回 3 本 ✅
DELETE /books/1 → 删除成功 ✅
GET /books → 只剩 2 本 ✅

---

## 五、当前进度

✅ FastAPI 路由
✅ CRUD 内存版
✅ 原生 SQL
✅ SQLAlchemy ORM
✅ FastAPI + 数据库整合
⬜ Pydantic 深入
⬜ 依赖注入

---

*2026-06-17 | 第7天*
