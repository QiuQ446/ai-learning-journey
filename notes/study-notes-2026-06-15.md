# 学习笔记 — 2026年6月15日

> 路线：纯 Python AI 应用开发 | 阶段：数据库入门（第5天）

---

## 一、今日完成的练习

| 文件 | 内容 | 状态 |
|------|------|------|
| practice/database/sql_basics.py | SQLite 原生 SQL：建表/增删改查 | ✅ 已跑通 |

---

## 二、SQLite 是什么

SQLite 是一个文件型数据库，Python 自带 sqlite3 模块，数据存在 test.db 文件里。

---

## 三、核心知识点

### 连接数据库
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

### 建表
CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, score INTEGER)

### 插入
INSERT INTO students VALUES (?, ?, ?)
conn.commit()  # 必须 commit！

### 查询
SELECT * FROM students WHERE score >= 80
cursor.fetchall()

### 更新
UPDATE students SET score = 95 WHERE name = '张三'
conn.commit()

### 删除
DELETE FROM students WHERE name = '王五'
conn.commit()

---

## 四、必须记住

| 关键点 | 作用 |
|--------|------|
| commit() | 数据写入硬盘 |
| fetchall() | 获取查询结果 |
| close() | 释放连接 |

---

## 五、当前进度

✅ FastAPI 路由
✅ CRUD 内存版
✅ 原生 SQL
⬜ SQLAlchemy ORM
⬜ FastAPI + 数据库

---

## 六、明日计划

- SQLAlchemy ORM 入门
- FastAPI + 数据库整合

---

*2026-06-15 | 第5天*
