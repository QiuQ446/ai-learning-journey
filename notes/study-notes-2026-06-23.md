# pytest 测试 — 2026年6月23日

> 路线：纯 Python AI 应用开发 | 阶段：测试（第11天）

---

## 一、今日学习的代码

| 文件 | 内容 | 状态 |
|------|------|------|
| practice/test_calc.py | pytest 基础：assert 断言 | ✅ 已跑通 |
| practice/test_book_api.py | 测试 FastAPI 接口 | ✅ 4 passed |

---

## 二、pytest 是什么

帮你自动测试代码，改完代码跑一下，1秒就知道有没有坏。

### 核心概念

| 概念 | 含义 |
|------|------|
| test_ 开头 | pytest 自动识别为测试 |
| assert | 断言，我坚信这是对的 |
| TestClient | 模拟 HTTP 请求，不用启动服务器 |

### 测试 API 示例

client = TestClient(app)
response = client.get('/books')
assert response.status_code == 200

---

## 三、测试结果

test_get_books ✅
test_create_book ✅
test_get_one_book ✅
test_delete_book ✅
4 passed in 1.87s

---

## 四、当前进度

✅ FastAPI 路由
✅ CRUD 内存版
✅ 原生 SQL
✅ SQLAlchemy ORM
✅ FastAPI + 数据库整合
✅ Pydantic 进阶
✅ 依赖注入 Depends
✅ async/await 异步
✅ pytest 测试
⬜ 项目结构
⬜ Docker 部署

---

*2026-06-23 | 第11天*
