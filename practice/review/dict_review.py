"""
题目：学生成绩管理系统（纯字典操作）

已知数据：
students = [
    {"name": "张三", "math": 85, "python": 90, "english": 78},
    {"name": "李四", "math": 92, "python": 88, "english": 95},
    {"name": "王五", "math": 76, "python": 82, "english": 80},
    {"name": "赵六", "math": 59, "python": 65, "english": 70},
    {"name": "孙七", "math": 88, "python": 91, "english": 85},
]

用字典和列表完成以下操作：
1. 统计每个学生的总分，存到新字段 "total"
2. 找出总分最高的学生，打印姓名和总分
3. 找出 Python 单科最高分的学生
4. 计算每门课的全班平均分（math_avg, python_avg, english_avg）
5. 筛选出有不及格科目（<60分）的学生姓名
6. 按总分从高到低排序，打印排名

要求：
- 不查资料，裸写
- 每道题写完就 print 验证结果
"""

students = [
    {"name": "张三", "math": 85, "python": 90, "english": 78},
    {"name": "李四", "math": 92, "python": 88, "english": 95},
    {"name": "王五", "math": 76, "python": 82, "english": 80},
    {"name": "赵六", "math": 59, "python": 65, "english": 70},
    {"name": "孙七", "math": 88, "python": 91, "english": 85},
]

1.
for s in students:
    s["total"] = s["math"] + s["python"] + s["english"]
 
print(students)
print()

2.
best = max(students,key = lambda s: s["total"])
print(f"总分最高：{best['name']},{best['total']}分")
print()

3.
best = max(students,key = lambda s: s["python"])
print(f"python最高:{best['name']},{best['python']}分")
print()

4.
math_avg = sum(s["math"] for s in students) / len(students)
python_avg = sum(s["python"] for s in students) / len(students)
english_avg = sum(s["english"] for s in students) / len(students)

5.
failed = []
for s in students:
    if s["math"] < 60 or s["python"] < 60 or s["english"] < 60:
        failed.append(s["name"])
print("有不及格科目:",failed)

6.
ranked = sorted(students, key=lambda s: s["total"],reverse=True)

for i, s in enumerate(ranked, start=1):
    print(f"第{i}名：{s['name']}，总分{s['total']}")