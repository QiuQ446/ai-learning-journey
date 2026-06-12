# 学习笔记 — 2026年6月12日

> 路线：纯 Python AI 应用开发 | 阶段：基础巩固（第2天）

---

## 一、今日完成的练习

| 文件 | 内容 | GitHub |
|------|------|--------|
| `practice/review/function_review.py` | 函数基础 6 道题 | ✅ 已提交 |

---

## 二、函数 6 题核心知识点

### 第1题：多条件判断（嵌套 if）

```python
def max_of_three(a, b, c):
    if a > b:
        if a >= c:
            return a
        else:
            return c
    if a <= b:
        if b >= c:
            return b
        else:
            return c
```

**思路：** 先比 a 和 b，再拿大的跟 c 比。两层嵌套 if 就能覆盖所有情况。

---

### 第2题：字符串反转 + 回文判断

```python
def is_palindrome(s):
    return s == s[::-1]
```

| 写法 | 结果 |
|------|------|
| `s[::-1]` | 反转字符串，"hello" → "olleh" |
| `s == s[::-1]` | 直接返回 True/False，无需 if-else |

---

### 第3题：字典统计词频

```python
def count_words(s):
    result = {}
    for word in s.split():
        if word in result:
            result[word] += 1    # 出现过，次数+1
        else:
            result[word] = 1     # 第一次出现，设为1
    return result
```

**执行过程拆解（输入 `"hello hello world"`）：**

| 循环 | word | result 状态 |
|------|------|-------------|
| 第1次 | `"hello"` | `{"hello": 1}` |
| 第2次 | `"hello"` | `{"hello": 2}` |
| 第3次 | `"world"` | `{"hello": 2, "world": 1}` |

> 进阶写法（一行）：`result[word] = result.get(word, 0) + 1`

---

### 第4题：列表推导式

```python
def filter_even(numbers):
    return [i for i in numbers if i % 2 == 0]
```

**`[i for i in numbers if i % 2 == 0]` 拆解：**

```
[ i           ← 要什么（元素本身）
  for i in numbers   ← 从哪拿
  if i % 2 == 0 ]    ← 什么条件
```

等价于：
```python
result = []
for i in numbers:
    if i % 2 == 0:
        result.append(i)
return result
```

---

### 第5题：字典映射替代 if-elif

```python
def grade_to_gpa(grade):
    mapping = {"优秀": 4.0, "良好": 3.0, "中等": 2.0, "及格": 1.0, "不及格": 0.0}
    return mapping[grade]
```

**为什么这样写？** 5个等级如果全用 if-elif 要写 10 行，字典映射 2 行搞定。数据驱动 > 逻辑分支。

---

### 第6题：闭包（函数返回函数）⭐ 今日难点

```python
def make_multiplier(n):
    def inner(x):
        return x * n
    return inner       # ← 返回的是一个函数

double = make_multiplier(2)
print(double(4))   # → 8
```

**核心理解：函数可以当变量一样 return 出去。**

| 步骤 | 发生了什么 |
|------|-----------|
| `make_multiplier(2)` | 造了一个 "×2 机器"，`n=2` 被锁在 `inner` 里面 |
| `double = ...` | `double` 变成了那个 "×2 机器" |
| `double(4)` | 调用这个机器，`4 × 2 → 8` |

**类比理解：**

```
make_multiplier(2)  →  给你一台 "×2 计算器"
make_multiplier(3)  →  给你一台 "×3 计算器"
make_multiplier(100) → 给你一台 "×100 计算器"
```

每台计算器都是独立的，你拿着它想算多少算多少。

---

## 三、已完成的复习进度

| 日期 | 文件 | 知识点 | 状态 |
|------|------|--------|------|
| 6.11 | `list_review.py` | 列表操作：max/min/sum/sort/遍历筛选/字典分级 | ✅ |
| 6.11 | `dict_review.py` | 字典嵌套：lambda/max+key/sorted/enumerate/推导式 | ✅ |
| 6.12 | `function_review.py` | 函数：嵌套if/字符串反转/词频统计/推导式/字典映射/闭包 | ✅ |

---

## 四、Git 操作备忘

```bash
git status
git add practice/review/xxx.py
git commit -m "描述信息"
git push origin main
```

---

## 五、明日计划

- [ ] 类（class）基础练习
- [ ] 文件 IO 练习
- [ ] 基础巩固收尾，准备进入 FastAPI 阶段

---

*笔记生成时间：2026-06-12 | 纯Python AI应用开发路线 | 第2天*