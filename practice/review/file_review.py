"""
题目：文件读写 + 异常处理 6 道题

每道题写完立刻运行验证
"""

# ===== 第1题：写文件 =====
# 写一个函数 write_greeting(name)
# 把 "你好，{name}！" 写入 greeting.txt 文件
# 调用3次，分别传入 张三、李四、王五
# 看看文件里是什么

def write_greeting(name):
    with open("greeting.txt","w",encoding="utf-8") as f:
        f.write(f"你好，{name}")
write_greeting("张三")
write_greeting("李四")
write_greeting("王五")  #文件里是 你好，王五

# "w" 模式每次都清空文件再写，所以张三被李四覆盖，李四被王五覆盖。
# 想要三行都保留，用 "a"（追加模式）

# ===== 第2题：读文件 =====
# 写一个函数 read_file(filename)
# 读取整个文件内容并打印出来
# 用第1题生成的 greeting.txt 测试
def read_file(filename):
    with open(filename,"r",encoding="utf-8") as f:
        content = f.read()
        print(content)
read_file("greeting.txt")


# ===== 第3题：逐行读写 =====
# 写一个函数 copy_file(source, target)
# 把源文件的内容逐行复制到目标文件
# 提示：f.readlines() 返回列表，每行是一个元素
def copy_file(source,target):
    with open(source,"r",encoding="utf-8") as f:
        contents = f.readlines()
    with open(target,"w",encoding="utf-8") as f:
        for content in contents:
            f.write(content)
copy_file("source.txt","target.txt")    #这两个的文件内容一样

# ===== 第4题：追加写入 =====
# 写一个函数 add_log(message)
# 每次调用时，把当前时间 + 消息追加到 log.txt 末尾
# 格式："2026-06-13 12:00:00 - {message}"
# 提示：from datetime import datetime; datetime.now()
from datetime import datetime

def add_log(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{now} - {message}\n")

# 测试
add_log("用户登录")
add_log("用户退出")

# ===== 第5题：安全的数字输入 =====
# 写一个函数 safe_input()
# 反复让用户输入数字，直到输入的是合法数字为止
# 输入了字母就提示"请输入数字！"并重试
# 用 try/except 捕获 ValueError
def safe_input():
    while True:
        try:
            return int(input("请输入数字："))
        except ValueError:
            print("请输入数字！")
safe_input()

# ===== 第6题：安全的文件读取 =====
# 写一个函数 safe_read(filename)
# 尝试读取文件，如果文件不存在就打印"文件不存在"
# 用 try/except 捕获 FileNotFoundError

def safe_read(filename):
    try:
        with open(filename,"r",encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("文件不存在")