# 学习笔记 — 2026年6月13日

> 路线：纯 Python AI 应用开发 | 阶段：基础巩固收尾（第3天）

---

## 一、今日完成的练习

| 文件 | 内容 | GitHub |
|------|------|--------|
| `practice/review/file_review.py` | 文件读写 + 异常处理 6 道题 | ✅ 已提交 |

---

## 二、文件读写核心知识

### 三个模式速查

| 模式 | 含义 | 什么场景用 |
|------|------|-----------|
| `"r"` | 读（read） | 读取已有文件 |
| `"w"` | 写（write）| 创建/覆盖文件 |
| `"a"` | 追加（append）| 在末尾添加内容，不删前面的 |

### 基本读写模板

```python
# 读文件
with open("文件名", "r", encoding="utf-8") as f:
    content = f.read()         # 一次性读全部
    # 或者
    lines = f.readlines()      # 按行读，返回列表

# 写文件（覆盖）
with open("文件名", "w", encoding="utf-8") as f:
    f.write("内容")

# 追加写（不覆盖）
with open("文件名", "a", encoding="utf-8") as f:
    f.write("追加的内容\n")
```

### `with open(...) as f:` 做了什么？

- `with` 自动管理文件开关，代码块结束后自动 `f.close()`
- `encoding="utf-8"` 处理中文必须加，否则乱码
- `f` 是文件对象，可以调用 `.read()`、`.readlines()`、`.write()`

---

### 第1题：写文件 ⚠️ 重要坑

```python
# ❌ 错误：每次都覆盖，最后只剩最后一个
def write_greeting(name):
    with open("greeting.txt", "w", encoding="utf-8") as f:
        f.write(f"你好，{name}")

# ✅ 正确：用 "a" 追加，加 \n 换行
def write_greeting(name):
    with open("greeting.txt", "a", encoding="utf-8") as f:
        f.write(f"你好，{name}\n")
```

**核心坑：** `"w"` 模式每次都清空文件，多个 `write_greeting()` 调用会互相覆盖。想要保留之前的内容，用 `"a"`。

---

### 第2题：读文件

```python
def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
```

最简单直接，一把读出全部内容。

---

### 第3题：逐行复制文件

```python
def copy_file(source, target):
    with open(source, "r", encoding="utf-8") as f:
        contents = f.readlines()       # 读成列表，每行一个元素
    with open(target, "w", encoding="utf-8") as f:
        for content in contents:
            f.write(content)           # 逐行写回去
```

---

### 第4题：日志追加

```python
from datetime import datetime

def add_log(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{now} - {message}\n")
```

| 步骤 | 代码 |
|------|------|
| 拿当前时间 | `datetime.now()` |
| 格式化成字符串 | `.strftime("%Y-%m-%d %H:%M:%S")` |
| 追加写 | `"a"` 模式 |
| 换行 | `\n` |

---

## 三、异常处理

### 基本模板

```python
try:
    # 可能出错的代码
    num = int(input("输入数字："))
except ValueError:
    # 如果出错了，执行这里
    print("不是数字！")
```

**核心思路：** 程序不因为一次错误就崩溃，`try` 里出问题直接跳到 `except`。

---

### 第5题：安全输入（循环重试）

```python
def safe_input():
    while True:
        try:
            return int(input("请输入数字："))
        except ValueError:
            print("请输入数字！")
```

**关键设计：**
- `while True` → 无限循环，直到输入正确
- `try` 里 `return` → 输入正确就跳出
- `except ValueError` → 输入不是数字，提示后继续循环

---

### 第6题：安全的文件读取

```python
def safe_read(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("文件不存在")
```

**常见易错：** `filename` 是字符串，不能直接 `.read()`，得先 `open(filename)` 拿到文件对象。

| 错误写法 | 正确写法 |
|----------|----------|
| `filename.read()` ❌ | `open(filename, "r").read()` ✅ |

---

## 四、常见异常类型速查

| 异常类型 | 什么时候触发 |
|----------|-------------|
| `ValueError` | 类型转换失败（如 `int("abc")`） |
| `FileNotFoundError` | 打开不存在的文件 |
| `ZeroDivisionError` | 除以 0 |
| `KeyError` | 字典访问不存在的 key |
| `IndexError` | 列表索引越界 |

---

## 五、Python 基础巩固阶段完成总结

| 日期 | 文件 | 知识点 | 状态 |
|------|------|--------|------|
| 6.11 | `list_review.py` | 列表操作：max/min/sum/sort/遍历筛选/字典分级 | ✅ |
| 6.11 | `dict_review.py` | 字典嵌套：lambda/max+key/sorted/enumerate/推导式 | ✅ |
| 6.12 | `function_review.py` | 函数：嵌套if/回文/词频/推导式/字典映射/闭包 | ✅ |
| 6.12 | `class_review.py` | 类：__init__/self/方法/列表装对象/状态变化 | ✅ |
| 6.13 | `file_review.py` | 文件读写：r/w/a 模式/逐行读写/日志追加 | ✅ |
| 6.13 | `file_review.py` | 异常处理：try/except/while True 重试 | ✅ |

**基础阶段全部过关，下一步进入 FastAPI 后端开发。**

---

## 六、明日计划

- [ ] FastAPI 入门：第一个接口、路由、请求参数
- [ ] 用 FastAPI 把之前的学生系统改造成 Web API

---

*笔记生成时间：2026-06-13 | 纯Python AI应用开发路线 | 第3天*