# 依赖注入 Depends — 2026年6月19日

> 路线：纯 Python AI 应用开发 | 阶段：代码优化（第9天）

---

## 一、今日完成的练习

| 文件 | 内容 | 状态 |
|------|------|------|
| practice/database/book_api_depends.py | Depends 依赖注入优化 CRUD | ✅ 已跑通 |

---

## 二、Depends 是什么

把重复代码抽出来，让 FastAPI 自动注入。

### 之前（手动管理）
每个函数都要写 Session(engine) 和 session.close()

### 之后（Depends）
def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()

路由参数加 session: Session = Depends(get_session)

---

## 三、对比

| | 旧版 | 新版 |
|------|------|------|
| 创建 session | 手动写 | 自动注入 |
| 关闭 session | 手动 close() | 自动关闭 |
| 忘记 close | 可能泄漏 | 不会 |

---

## 四、yield 的理解

yield 就是暂停，先去忙，忙完回来收尾

---

## 五、当前进度

✅ FastAPI 路由
✅ CRUD 内存版
✅ 原生 SQL
✅ SQLAlchemy ORM
✅ FastAPI + 数据库整合
✅ Pydantic 进阶
✅ 依赖注入 Depends
⬜ 异步编程
⬜ 测试

---

*2026-06-19 | 第9天*
