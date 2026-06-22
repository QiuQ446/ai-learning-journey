"""
测试 FastAPI 接口
"""
from fastapi.testclient import TestClient
import sys
sys.path.insert(0, '.')
from database.book_api_depends import app

client = TestClient(app)  # 不用真正启动服务器！


def test_get_books():
    """测试查全部"""
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # 返回的是列表


def test_create_book():
    """测试新增"""
    response = client.post("/books", json={
        "title": "测试书",
        "author": "测试作者",
        "pages": 100
    })
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "添加成功"
    assert data["book"]["title"] == "测试书"


def test_get_one_book():
    """测试查一本"""
    response = client.get("/books/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "title" in data


def test_delete_book():
    """测试删除"""
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json()["message"] == "删除成功"