# 学习笔记 — 2026年6月15日

> 路线：纯 Python AI 应用开发 | 阶段：数据库入门（第5天）

---

## 一、今日完成的练习

| 文件 | 内容 | GitHub |
|------|------|--------|
| `practice/database/sql_basics.py` | SQLite 原生 SQL：建表/增删改查 | ✅ 已跑通 |

---

## 二、SQLite 是什么

SQLite 是一个**文件型数据库**，不需要安装任何服务器软件，Python 自带 `sqlite3` 模块。

```
你的数据存在 test.db 文件里
关了电脑，数据还在
重启 Python，数据还在
```

---

## 三、sql_basics.py 完整代码

```python
import sqlite3

# 1. 连接数据库（文件不存在会自动创建）
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# 2. 建表
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER,
        age INTEGER
    )
""")

# 3. 插入数据
cursor.execute("INSERT INTO students (name, score, age) VALUES (?, ?, ?)", ("张三", 85, 20))
cursor.execute("INSERT INTO students (name, score, age) VALUES (?, ?, ?)", ("李四", 92, 21))
cursor.execute("INSERT INTO students (name, score, age) VALUES (?, ?, ?)", ("王五", 78, 19))
conn.commit()   # ← 必须 commit，否则数据不会真正写入硬盘

# 4. 查询所有
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("全部学生：")
for row in rows:
    print(row)   # 每一行是一个元组 (id, name, score, age)

# 5. 条件查询：分数 >= 80
cursor.execute("SELECT name, score FROM students WHERE score >= 80")
print("\n分数 >= 80：")
for row in cursor.fetchall():
    print(row)

# 6. 更新数据
cursor.execute("UPDATE students SET score = 95 WHERE name = '张三'")
conn.commit()

# 7. 删除数据
cursor.execute("DELETE FROM students WHERE name = '王五'")
conn.commit()

# 8. 验证：再看一次全部
cursor.execute("SELECT * FROM students")
print("\n操作后：")
for row in cursor.fetchall():
    print(row)

# 9. 关闭连接
conn.close()
```

---

## 四、核心知识点

### 连接数据库

```python
conn = sqlite3.connect("test.db")   # 连接（文件不存在会自动创建）
cursor = conn.cursor()              # 获取游标，用来执行 SQL
```

### 建表

```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER,
        age INTEGER
    )
""")
```

| 字段类型 | 含义 |
|----------|------|
| `INTEGER` | 整数 |
| `TEXT` | 字符串 |
| `PRIMARY KEY AUTOINCREMENT` | 主键，自动递增 |
| `NOT NULL` | 不能为空 |

### 插入数据（INSERT）

```python
cursor.execute("INSERT INTO students (name, score, age) VALUES (?, ?, ?)", ("张三", 85, 20))
conn.commit()   # ← 必须 commit
```

**`?` 是占位符**，防止 SQL 注入。后面的元组 `"张三", 85, 20` 会自动填进去。

### 查询数据（SELECT）

```python
# 查全部
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()   # 返回列表，每行是一个元组

# 条件查询
cursor.execute("SELECT name, score FROM students WHERE score >= 80")
```

### 更新数据（UPDATE）

```python
cursor.execute("UPDATE students SET score = 95 WHERE name = '张三'")
conn.commit()
```

### 删除数据（DELETE）

```python
cursor.execute("DELETE FROM students WHERE name = '王五'")
conn.commit()
```

---

## 五、必须记住的 3 个关键点

| 关键点 | 代码 | 为什么重要 |
|--------|------|-----------|
| **commit()** | `conn.commit()` | 不 commit，数据只在内存里，不会写入硬盘 |
| **fetchall()** | `cursor.fetchall()` | 把查询结果拿出来，否则看不到 |
| **close()** | `conn.close()` | 释放连接，否则数据库文件被锁定 |

---

## 六、SQL 速查表

| 操作 | SQL 语句 | Python 调用 |
|------|----------|-------------|
| 建表 | `CREATE TABLE 表名 (列名 类型, ...)` | `cursor.execute(...)` |
| 增 | `INSERT INTO 表名 (列) VALUES (?, ?)` | `cursor.execute(..., (值1, 值2))` |
| 查 | `SELECT 列 FROM 表 WHERE 条件` | `cursor.execute(...); cursor.fetchall()` |
| 改 | `UPDATE 表 SET 列=值 WHERE 条件` | `cursor.execute(...); conn.commit()` |
| 删 | `DELETE FROM 表 WHERE 条件` | `cursor.execute(...); conn.commit()` |

---

## 七、运行结果

```
全部学生：
(1, '张三', 85, 20)
(2, '李四', 92, 21)
(3, '王五', 78, 19)

分数 >= 80：
('张三', 85)
('李四', 92)

操作后：
(1, '张三', 95, 20)    ← 分数被更新为 95
(2, '李四', 92, 21)    ← 王五被删除了
```

---

## 八、当前进度

```
✅ HTTP 原理（requests 发请求）
✅ FastAPI 路由（路径参数、查询参数、请求体）
✅ 完整 CRUD（GET/POST/DELETE）—— 内存版
✅ 原生 SQL（sqlite3 增删改查）
⬜ SQLAlchemy ORM（对象操作数据库）
⬜ FastAPI + 数据库整合（持久化）
⬜ Pydantic 深入（校验、可选字段）
⬜ 依赖注入 + 中间件
⬜ 异步编程
⬜ 测试
⬜ 项目结构 + Docker 部署
```

---

## 九、明日计划

- [ ] SQLAlchemy ORM 入门：把 SQL 变成 Python 对象操作
- [ ] FastAPI + 数据库整合：让 books API 数据持久化
- [ ] 理解 ORM 和原生 SQL 的区别

---

*笔记生成时间：2026-06-15 | 纯Python AI应用开发路线 | 第5天*