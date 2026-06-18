"""
Pydantic 进阶练习
"""

from pydantic import BaseModel, Field
from typing import Optional

# 1. 基础校验：限制长度和范围
class Book(BaseModel):
    title: str = Field(..., min_length=1, max_length=50, description="书名")
    author: str = Field(..., min_length=1, max_length=20, description="作者")
    pages: int = Field(..., ge=1, le=9999, description="页数")

# 2. 可选字段
class BookUpdate(BaseModel):
    title: Optional[str] = None   # 可以不填，不填就是 None
    author: Optional[str] = None
    pages: Optional[int] = None

# 3. 默认值
class BookWithDefault(BaseModel):
    title: str
    author: str
    pages: int = 100         # 不填默认 100

# ===== 测试 =====
if __name__ == "__main__":
    # 测试 1：正常数据
    book1 = Book(title="Python入门", author="小明", pages=300)
    print("✅ 正常创建:", book1)

    # 测试 2：title 太短（空字符串）
    try:
        book2 = Book(title="", author="小明", pages=300)
    except Exception as e:
        print("❌ 错误:", e)

    # 测试 3：pages 超出范围
    try:
        book3 = Book(title="好书", author="小明", pages=99999)
    except Exception as e:
        print("❌ 错误:", e)

    # 测试 4：可选字段
    update = BookUpdate(title="新书名")  # 只改 title
    print("✅ 可选更新:", update)

    # 测试 5：默认值
    book4 = BookWithDefault(title="默认页数", author="小明")
    print("✅ 默认页数:", book4.pages)