# Pydantic 进阶 — 2026年6月18日

> 路线：纯 Python AI 应用开发 | 阶段：数据校验（第8天）

---

## 一、今日完成的练习

| 文件 | 内容 | 状态 |
|------|------|------|
| practice/pydantic_practice.py | Pydantic 校验、可选字段、默认值 | ✅ 已跑通 |

---

## 二、核心知识点

### 限制长度
title: str = Field(..., min_length=1, max_length=50)

### 限制范围
pages: int = Field(..., ge=1, le=9999)

### 可选字段
title: Optional[str] = None  # 可以不填

### 默认值
pages: int = 100  # 不填默认 100

### 必填
Field(...)  # 三个点表示必填

---

## 三、Field 参数速查

| 参数 | 含义 | 示例 |
|------|------|------|
| min_length | 最小长度 | min_length=1 |
| max_length | 最大长度 | max_length=50 |
| ge | 大于等于 | ge=1 |
| le | 小于等于 | le=9999 |
| gt | 大于 | gt=0 |
| lt | 小于 | lt=100 |

---

## 四、测试结果

正常创建 → ✅ 通过
title 为空 → ❌ 拒绝（最少1个字符）
pages 超范围 → ❌ 拒绝（最多9999）
可选更新 → ✅ 只改需要的字段
默认值 → ✅ 不填用默认 100

---

## 五、当前进度

✅ FastAPI 路由
✅ CRUD 内存版
✅ 原生 SQL
✅ SQLAlchemy ORM
✅ FastAPI + 数据库整合
✅ Pydantic 进阶
⬜ 依赖注入
⬜ 异步编程
⬜ 测试

---

*2026-06-18 | 第8天*
