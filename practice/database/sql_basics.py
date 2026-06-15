"""
SQL 基础练习 —— 用 Python 内置的 sqlite3

不需要 pip install 任何东西，Python 自带
"""

import sqlite3

# 1.连接数据库（文件不存在会自动创建）
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