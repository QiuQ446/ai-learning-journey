"""数据库连接 + 依赖注入"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase

# 数据库连接
SQLALCHEMY_DATABASE_URL = "sqlite:///books.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)

# 基类
class Base(DeclarativeBase):
    pass

# 依赖注入函数
def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()