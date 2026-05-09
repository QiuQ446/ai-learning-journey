from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "你好，邱权！FastAPI 启动成功！"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"你好，{name}！"}

@app.get("/greet")
def greet(name: str, times: int = 1):
    """查询参数示例：/greet?name=邱权&times=3"""
    greeting = f"你好，{name}！"
    return {"message": greeting * times}


@app.get("/search")
def search(keyword: str, page: int = 1, size: int = 10):
    """查询参数示例：/search?keyword=Python&page=2&size=5"""
    return {
        "keyword": keyword,
        "page": page,
        "size": size,
        "result": f"正在搜索「{keyword}」，第 {page} 页，每页 {size} 条"
    }