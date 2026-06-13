"""
HTTP 基础练习

用 requests 库探索 HTTP 协议
"""

import requests

# 1. GET 请求，打印状态码和响应头
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(f"状态码: {response.status_code}")
print(f"Content-Type: {response.headers['Content-Type']}")
print(f"响应体: {response.json()}")

# 2. GET 请求不存在的页面，观察状态码
response = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
print(f"不存在的页面状态码: {response.status_code}")

# 3. POST 请求，发送 JSON 数据
data = {"title": "我的第一篇文章", "body": "这是内容", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(f"POST 状态码: {response.status_code}")
print(f"返回数据: {response.json()}")

# 4. 4个常见错误码实验
print("\n--- 状态码实验 ---")
print(f"200 OK: {requests.get('https://jsonplaceholder.typicode.com/posts/1').status_code}")
print(f"404 Not Found: {requests.get('https://jsonplaceholder.typicode.com/notexist').status_code}")