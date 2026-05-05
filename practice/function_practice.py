"""

基本函数：def greet(name): 返回 "你好, " + name

返回值：写一个计算两数之和的函数，用 return 返回结果

多种参数：

默认参数：def power(base, exp=2): 默认平方

关键字参数：调用时指定参数名，打乱顺序

*args：接收任意数量位置参数，打包成元组

**kwargs：接收任意数量关键字参数，打包成字典

"""

# 1.基本函数定义与调用

def greet(name):
    return "你好，"+ name

# 调用基本函数
print("=== 1. 基本函数 ===")
print(greet("小明"))
print(greet("小红"))


# 2.带返回值的函数（计算两数之和）

def add(a,b):
    return a + b  
                # return 会把计算结果返回给调用处

# 调用并接收返回值
print("\n=== 2. 返回值函数 ===")
result = add(10, 20)
print("10 + 20 =",result)
print("5 + 7 =",add(5, 7))  
                # 直接在 print 中调用函数

# 3.默认参数（不传参时使用默认值）
def power(base,exp=2):
    # exp 默认是 2，也就是平方
    return base ** exp

print("\n=== 3. 默认参数 ===")
print("5 的平方 = ",power(5))
                    # 不传入 exp 参数，使用默认值 2
print("3 的立方 = ",power(3, exp=3))    
                    # 传入 exp 参数覆盖默认值


# 4. 关键字参数（调用时指定参数名，顺序可打乱）

def introduce(name, age, city):
    return f"我叫{name}，今年{age}岁，来自{city}"

print("\n=== 4. 关键字参数 ===")
# 正常顺序
print(introduce("小明", 21, "广西"))
# 打乱顺序，使用参数名,依然正确
print(introduce(city="广东",name="小丽",age=20))

# 5.*args (接收任意数量位置参数，打包成元组)
def sum_all(*args):
    # *args 会把所有位置参数打包成一个元组
    total = 0
    for num in args:
        total += num
    return total

print("\n=== 5. *args 任意位置参数 ===")
print("1 + 2 + 3=",sum_all(1,2,3))
print("1+2+3+4 =", sum_all(1, 2, 3, 4))
print("10+20+30 =", sum_all(10, 20, 30))

# 6. **kwargs (接收任意数量关键字参数，打包成字典)
def print_info(**kwargs):
    # **kwargs 会把所有关键字参数打包成一个字典
    #kwargs 是一个字典，可以通过键访问对应的值
    print("收到的信息：", kwargs)
    # 遍历字典
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print("\n=== 6. **kwargs 任意关键字参数 ===")
print_info(name="Alice",age=21,city="北京")
print_info(name="Bob",hobby="篮球",country="美国")
print_info(book="Python入门", price=59, publisher="某某出版社")

                         
      