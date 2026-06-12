# 学习笔记 — 2026年6月11日

> 路线：纯 Python AI 应用开发 | 阶段：基础巩固（第1天）

---

## 一、今日完成的练习

| 文件 | 内容 | GitHub |
|------|------|--------|
| `practice/review/list_review.py` | 列表基础操作，6道题 | ✅ 已提交 |
| `practice/review/dict_review.py` | 字典嵌套列表操作，6道题 | ✅ 已提交 |

---

## 二、列表操作（list_review.py 核心知识点）

### 常用操作速查

```python
scores = [85, 92, 78, 95, 88, 72, 90, 83]

max(scores)          # 最大值 → 95
min(scores)          # 最小值 → 72
sum(scores)          # 求和 → 683
len(scores)          # 长度 → 8
sum(scores)/len(scores)  # 平均值 → 85.375
scores.sort()        # 原地排序（从小到大）
```

### 遍历 + 条件筛选

```python
count = 0
for i in scores:
    if i >= 60:
        count += 1
# count = 8（全部及格）
```

### 创建字典存分级结果

```python
grades = {}
for score in scores:
    if score >= 90:
        grades[score] = '优秀'
    elif score >= 80:
        grades[score] = '良好'
    elif score >= 70:
        grades[score] = '中等'
    elif score >= 60:
        grades[score] = '及格'
    else:
        grades[score] = '不及格'
```

> ⚠️ **注意**：不要用 `dict` 当变量名，会覆盖 Python 内置的 `dict` 类型。

---

## 三、字典嵌套列表（dict_review.py 核心知识点）

### 数据结构理解

```python
students = [
    {"name": "张三", "math": 85, "python": 90, "english": 78},
    {"name": "李四", "math": 92, "python": 88, "english": 95},
    ...
]
```

**理解方法：** 大列表 `[ ]` 装小字典 `{ }`，每个字典是一行数据，像一个 Excel 表格。

| 取值方式 | 结果 |
|----------|------|
| `students[0]` | 张三的整个字典 |
| `students[0]["name"]` | `"张三"` |
| `students[0]["math"]` | `85` |

---

### 核心操作1：遍历中给字典加新字段

```python
for s in students:
    s["total"] = s["math"] + s["python"] + s["english"]
```

**关键理解：** `s` 直接指向列表里的原字典，`s["total"] = ...` 会直接修改原数据。循环结束后每个学生字典都多了 `"total"` 字段。

---

### 核心操作2：max() 按某个字段找最大

```python
best = max(students, key=lambda s: s["total"])
```

**`lambda s: s["total"]` 拆解：**

| 部分 | 含义 |
|------|------|
| `lambda` | 关键字，表示"临时造一个函数" |
| `s` | 参数名（每次传入一个学生字典） |
| `s["total"]` | 函数体，返回这个学生的总分 |
| `key=` | 告诉 max "按这个规则比大小" |

等价写法：
```python
def get_total(s):
    return s["total"]

best = max(students, key=get_total)
```

---

### 核心操作3：sorted() 按某个字段排序

```python
ranked = sorted(students, key=lambda s: s["total"], reverse=True)
```

| 参数 | 作用 |
|------|------|
| `students` | 要排序的列表 |
| `key=lambda s: s["total"]` | 按 total 字段比较 |
| `reverse=True` | 从大到小（不加则从小到大） |

---

### 核心操作4：enumerate() 带编号遍历

```python
for i, s in enumerate(ranked, start=1):
    print(f"第{i}名：{s['name']}，总分{s['total']}")
```

| 循环次数 | `i` | `s` |
|----------|-----|-----|
| 第1次 | 1 | 李四的字典 |
| 第2次 | 2 | 孙七的字典 |
| ... | ... | ... |

`start=1` 让编号从 1 开始，不写默认从 0 开始。

---

### 核心操作5：生成器表达式求平均

```python
math_avg = sum(s["math"] for s in students) / len(students)
```

**大脑中的执行过程：**

```
第一步：遍历 students，取出每个 math 成绩
  → [85, 92, 76, 59, 88]

第二步：sum() 加起来
  → 85 + 92 + 76 + 59 + 88 = 400

第三步：除以人数
  → 400 / 5 = 80.0
```

---

### 核心操作6：列表推导式筛选

```python
failed = [s["name"] for s in students 
          if s["math"] < 60 or s["python"] < 60 or s["english"] < 60]
```

等价于：
```python
failed = []
for s in students:
    if s["math"] < 60 or s["python"] < 60 or s["english"] < 60:
        failed.append(s["name"])
```

---

## 四、今日易错点

| 错误 | 为什么错 | 正确做法 |
|------|----------|----------|
| `dict = {}` | 覆盖了 Python 内置类型 `dict` | 用 `grades`、`result`、`data` 等 |
| 算了 `count` 没打印 | 变量计算了但没输出，看不到结果 | 加 `print(count)` |
| 循环打印用 `end=" "` 后没换行 | 后续输出会粘在同一行 | 末尾加一个 `print()` 换行 |

---

## 五、Git 操作备忘

```bash
git status                          # 查看改了哪些文件
git add practice/review/xxx.py      # 只添加你要提交的文件
git commit -m "描述信息"             # 提交到本地
git push origin main                # 推到 GitHub
```

---

## 六、明日计划

- [ ] 期中考试（Python 前5章）
- [ ] 考试结束后，继续基础巩固：函数 + 类 + 文件IO

---

*笔记生成时间：2026-06-11 | 纯Python AI应用开发路线 | 第1天*