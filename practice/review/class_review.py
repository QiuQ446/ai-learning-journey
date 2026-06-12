"""
题目：类（class）基础 6 道题 —— 从零开始

要求：每道题写完立刻创建对象验证
"""

# ===== 第1题：你的第一个类 =====
# 定义一个 Dog 类，有 name 和 age 两个属性
# 创建两只狗，打印它们的名字
1.
class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
dog1 = dog("哈士奇",2)
dog2 = dog("吉娃娃",2)

print(dog1.name)
print(dog2.name)
        
# ===== 第2题：类里面加方法 =====
# 给 Dog 类加一个 bark() 方法，调用时打印 "汪汪！我是xx"
# 提示：方法就是在类里面定义的函数，第一个参数必须是 self
2.
class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"汪汪！我是{self.name}")
dog3 = dog("大黄",1)
dog3.bark()

        
# ===== 第3题：能计算的类 =====
# 定义一个 Rectangle 类，有 width 和 height
# 加一个 area() 方法，返回面积
# 加一个 perimeter() 方法，返回周长
3.
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width + self.height)
rectangle1 = Rectangle(3,4)
rectangle1.area()
rectangle1.perimeter()
print(rectangle1.area())       # → 12
print(rectangle1.perimeter())  # → 14

# ===== 第4题：列表里装对象 =====
# 用第3题的 Rectangle 类
# 创建3个矩形，放进列表，用循环打印每个矩形的面积
4.
rectangle_list = [Rectangle(4,4),Rectangle(2,5),Rectangle(3,6)]
for i in rectangle_list:
    print(i.area())


# ===== 第5题：学生类 =====
# 定义一个 Student 类，有 name 和 score
# 加一个 is_pass() 方法，score >= 60 返回 True
# 创建5个学生放进列表，筛选出及格的学生名字
5.
class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def is_pass(self):
        return self.score >= 60
student_list = [Student("aa",66),Student("bb",77),Student("cc",56),Student("dd",87),Student("ee",44)]
for student in student_list:
    if student.is_pass():
        print(student.name,end=" ")


# ===== 第6题：银行账户 =====
# 定义一个 BankAccount 类
# __init__ 接收 name 和 balance（初始余额）
# 加一个 deposit(amount) 方法：存钱
# 加一个 withdraw(amount) 方法：取钱（余额不足时打印"余额不足"）
# 加一个 show() 方法：打印 "xx 的余额：xxx 元"
6.
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if self.balance >=amount:
            self.balance -= amount
        else:
            print("余额不足")
    def show(self):
        print(f"{self.name}的余额：{self.balance}元")


