import os
from dotenv import load_dotenv

# 加载 .env 文件里的所有变量
load_dotenv()

# 像用普通变量一样读取密钥
api_key = os.getenv("DEEPSEEK_API_KEY")
my_name = os.getenv("MY_NAME")

print(f"我的名字是：{my_name}")
print(f"API Key 是：{api_key[:10]}...（已隐藏后半段）")