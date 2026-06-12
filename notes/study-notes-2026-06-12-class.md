# 学习笔记 — 2026年6月12日（续）

> 路线：纯 Python AI 应用开发 | 阶段：基础巩固（第2天 · 晚间）

---

## 一、今日完成的练习

| 文件 | 内容 | GitHub |
|------|------|--------|
| `practice/review/function_review.py` | 函数基础 6 道题 | ✅ 已提交 |
| `practice/review/class_review.py` | 类（class）基础 6 道题 | ✅ 已提交 |

---

## 二、类（class）核心知识点

### 三个核心概念

| 概念 | 一句话 | 代码 |
|------|--------|------|
| `class` | 模板，定义"一类东西" | `class Dog:` |
| `__init__` | 出厂设置，创建对象时自动运行 | `def __init__(self, name, age):` |
| `self` | "我自己"，当前这个对象 | `self.name = name` |

### 大白话类比

```
类 = 月饼模具
对象 = 用模具压出来的月饼
self = 指代"当前这块月饼"
```

```python
class Dog:
    def __init__(self, name, age):
        self.name = name    # 这个狗的名字
        self.age = age      # 这个狗的年龄

d1 = Dog("旺财", 3)    # 压出第一块月饼
d2 = Dog("小白", 1)    # 压出第二块月饼
```

---

### 第1题：定义类 + 创建对象

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("哈士奇", 2)
dog2 = Dog("吉娃娃", 2)
print(dog1.name)   # → 哈士奇
```

> ⚠️ 类名建议首字母大写（`Dog` 而不是 `dog`），Python 惯例。

---

### 第2题：类里面加方法

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"汪汪！我是{self.name}")   # ← 注意 self.name，不是 name

dog3 = Dog("大黄", 1)
dog3.bark()   # → 汪汪！我是大黄
```

**方法 vs 函数：** 类里面定义的函数叫方法，第一个参数必须是 `self`。

> ⚠️ 易错：`print(f"汪汪！我是{self.name}")` 不能写成 `print(f"汪汪！我是{name}")`，忘了 `self.` 会报错。

---

### 第3题：能计算返回值的类

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height        # 面积

    def perimeter(self):
        return 2 * (self.width + self.height)  # 周长

r = Rectangle(3, 4)
print(r.area())       # → 12
print(r.perimeter())  # → 14
```

> ⚠️ 易错：方法里 `return` 了值，调用时要用 `print()` 才能看到。

---

### 第4题：列表里装对象

```python
rectangles = [Rectangle(4, 4), Rectangle(2, 5), Rectangle(3, 6)]
for r in rectangles:
    print(r.area())
```

对象可以像普通数据一样放进列表、遍历、调用方法。这跟之前字典列表嵌套是一样的套路。

---

### 第5题：方法返回布尔值 + 筛选

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_pass(self):
        return self.score >= 60

students = [Student("aa", 66), Student("bb", 77), Student("cc", 56),
            Student("dd", 87), Student("ee", 44)]

for s in students:
    if s.is_pass():
        print(s.name, end=" ")
```

---

### 第6题：有状态变化的类（银行账户）

```python
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount          # 余额增加

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount       # 余额减少
        else:
            print("余额不足")

    def show(self):
        print(f"{self.name}的余额：{self.balance}元")
```

**关键理解：** `deposit` 和 `withdraw` 会**改变 `self.balance` 的值**，这个值在对象的整个生命周期内保持。这就是"对象有状态"。

---

## 三、今日易错点

| 错误 | 原因 | 正确写法 |
|------|------|----------|
| `print("汪汪{name}")` | 忘了 f-string 的 `f` | `print(f"汪汪{self.name}")` |
| `print("汪汪{self.name}")` | 有 `f` 但变量名忘了 `self.` | 同上 |
| 周长 `w + h` | 忘了乘 2 | `2 * (w + h)` |
| 调方法没 `print` | 方法 return 了值但没输出 | `print(r.area())` |
| `self.balence` | 拼写错误 | `self.balance` |

---

## 四、基础巩固阶段总结（6.11 — 6.12）

| 日期 | 文件 | 知识点 | 掌握程度 |
|------|------|--------|----------|
| 6.11 | `list_review.py` | 列表操作：max/min/sum/sort/遍历/字典分级 | ✅ |
| 6.11 | `dict_review.py` | 字典嵌套：lambda/max+key/sorted/enumerate/推导式 | ✅ |
| 6.12 | `function_review.py` | 函数：嵌套if/回文/词频/推导式/字典映射/闭包 | ✅ |
| 6.12 | `class_review.py` | 类：__init__/self/方法/列表装对象/状态变化 | ✅ |

**Python 四大基础全部过完，下一步进入文件 IO 和异常处理，然后冲向 FastAPI。**

---

## 五、明日计划

- [ ] 文件 IO 练习（读/写/JSON 序列化）
- [ ] 异常处理（try/except）
- [ ] 基础巩固收尾，准备进入 FastAPI

---

*笔记生成时间：2026-06-12 | 纯Python AI应用开发路线 | 第2天*