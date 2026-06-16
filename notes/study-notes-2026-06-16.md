# ORM的增删查改 — 2026年6月16日

> 路线：纯 Python AI 应用开发 | 阶段：数据库入门（第6天）

---

## 一、今日完成的练习

| 文件 | 内容 | 状态 |
|------|------|------|
| practice/database/orm_practice.py | SQLAlchemy ORM 增删查改 | ✅ 已跑通 |

---

## 二、ORM 是什么

ORM = Object Relational Mapping（对象关系映射）

把数据库表映射成 Python 类，把数据库行映射成 Python 对象。

不用写 SQL，直接操作 Python 对象！

---

## 三、ORM vs 原生 SQL 对比

| 操作 | 原生 SQL | ORM |
|------|----------|-----|
| 增 | INSERT INTO ... VALUES (?, ?) | session.add(Student(...)) |
| 查 | SELECT * FROM ... WHERE ... | session.query(Student).filter(...) |
| 改 | UPDATE ... SET ... WHERE ... | 对象.属性 = 新值 |
| 删 | DELETE FROM ... WHERE ... | session.delete(对象) |

---

## 四、ORM 核心代码

### 定义模型（类 = 表）
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

### 增
session.add(Student(name='张三', score=85))
session.commit()

### 查
students = session.query(Student).all()
session.query(Student).filter(Student.score >= 80).all()

### 改
zhangsan = session.query(Student).filter(Student.name == '张三').first()
zhangsan.score = 95
session.commit()

### 删
wangwu = session.query(Student).filter(Student.name == '王五').first()
session.delete(wangwu)
session.commit()

---

## 五、必须记住

| 关键点 | 作用 |
|--------|------|
| session.add() | 添加对象 |
| session.commit() | 提交，写入数据库 |
| session.query().all() | 查全部 |
| session.query().filter() | 条件查询 |
| session.delete() | 删除对象 |

---

## 六、运行结果

已插入3个学生
全部学生
1|张三|85分
2|李四|92分
3|王五|78分
张三分数改为 95
删除了王五
最终数据:
1 | 张三 | 95分
2 | 李四 | 92分

---

## 七、当前进度

✅ FastAPI 路由
✅ CRUD 内存版
✅ 原生 SQL
✅ SQLAlchemy ORM
⬜ FastAPI + 数据库整合

---

*2026-06-16 | 第6天*
