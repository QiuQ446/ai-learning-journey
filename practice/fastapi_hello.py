from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "你好，邱权！FastAPI 启动成功！"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"你好，{name}！"}