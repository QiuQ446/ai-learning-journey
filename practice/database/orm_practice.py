"""
ORM 练习 —— SQLAlchemy
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, DeclarativeBase

# 1. 连接数据库
engine = create_engine('sqlite:///orm_test.db', echo=False)

# 2. 定义基类
class Base(DeclarativeBase):
    pass

# 3. 定义模型（类 = 表）
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    score = Column(Integer)
    age = Column(Integer)

# 4. 创建表
Base.metadata.create_all(engine)

# 5. 创建 session
session = Session(engine)

# 增：创建3个学生，add，commit
session.add(Student(name='张三',score=85,age=20))
session.add(Student(name='李四',score=92,age=21))
session.add(Student(name='王五',score=78,age=19))

session.commit()
print('已插入3个学生')


# 查：query(Student).all()
students = session.query(Student).all()
print('全部学生')
for s in students:
    print(f'{s.id}|{s.name}|{s.score}分')


# ===== 改 =====
zhangsan = session.query(Student).filter(Student.name == '张三').first()
zhangsan.score = 95
session.commit()
print('张三分数改为 95')


# ===== 删 =====
wangwu = session.query(Student).filter(Student.name == '王五').first()
session.delete(wangwu)
session.commit()
print('删除了王五')


# ===== 验证 =====
print('最终数据:')
for s in session.query(Student).all():
    print(f'{s.id} | {s.name} | {s.score}分')



session.close()