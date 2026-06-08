import sqlite3

# 1. 连接数据库（文件不存在会自动创建）
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# 2. 建表
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        score REAL NOT NULL,
        grade TEXT DEFAULT '大一'
    )
""")

# 3. 插入一条数据
cursor.execute("INSERT INTO students (name, score) VALUES (?, ?)", ("邱权", 95))
conn.commit()

# 4. 查询所有数据
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 5. 关闭连接
conn.close()