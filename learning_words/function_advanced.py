"""
默认参数：写一个 def greet(name, greeting="你好")，调用时如果不传第二个参数就用默认值

关键字参数：写一个 def student_info(name, age, school)，调用时故意打乱顺序传参，如 student_info(age=19, school="广西民族大学", name="邱权")

感受：默认参数让函数更灵活，关键字参数让调用更清晰

"""

def greet(name, greeting="你好"):
    return f"{greeting}，{name}！"

print(greet("小明"))  # 使用默认问候语,输出 "你好，小明！"
print(greet("小红", greeting="欢迎"))  # 使用自定义问候语


def student_info(name, age, school):
    return f"我叫{name}，今年{age}岁，来自{school}"

print(student_info(age=19, school="广西民族大学", name="邱权"))






"""

*args：写一个 def sum_all(*args)，接收任意多个数字，返回它们的和。调用 sum_all(1,2,3,4,5) 验证

**kwargs：写一个 def build_profile(**kwargs)，接收任意多个键值对，打印出来。调用 build_profile(name="邱权", skill="Python", goal="AI工程师")

核心感受：*args 把多个值打包成元组，**kwargs 把多个键值对打包成字典

"""

def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3,4,5))  # 输出 15



def build_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")    

build_profile(name="邱权", skill="Python", goal="AI工程师")