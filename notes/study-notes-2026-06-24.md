# 项目结构规范化 — 2026年6月24日

> 路线：纯 Python AI 应用开发 | 阶段：项目结构（第12天）

---

## 一、今日完成

| 任务 | 状态 |
|------|------|
| 创建 app/ 标准项目结构 | ✅ |
| database.py 数据库连接 | ✅ |
| models.py 数据库模型 | ✅ |
| schemas.py Pydantic 模型 | ✅ |
| routers/books.py 路由 | ✅ |
| main.py 入口文件 | ✅ |
| 启动测试通过 | ✅ |

---

## 二、之前 vs 之后

| | 之前 | 之后 |
|------|------|------|
| 代码 | 1个文件 74行 | 5个文件 各<30行 |
| 启动 | uvicorn practice...book_api_depends:app | uvicorn app.main:app |
| 响应 | 手动写 dict | response_model 自动 |

---

## 三、新结构

app/
├── main.py          ← 入口
├── database.py      ← 数据库 + Depends
├── models.py        ← 表定义
├── schemas.py       ← 数据校验
└── routers/
    └── books.py     ← 路由

## 四、关键变化

@router 代替 @app
APIRouter 代替 FastAPI
app.include_router() 注册路由
response_model= 自动生成文档

---

## 五、当前进度

✅ FastAPI 路由
✅ CRUD 内存版
✅ 原生 SQL
✅ SQLAlchemy ORM
✅ FastAPI + 数据库
✅ Pydantic 进阶
✅ Depends 依赖注入
✅ async/await 异步
✅ pytest 测试
✅ 项目结构规范化
⬜ Docker 部署

---

*2026-06-24 | 第12天*
