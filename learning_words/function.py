"""

函数定义、调用、参数、return 返回值、函数求阶乘、判断素数

"""

############                        函数定义与调用

def say_hello():
    print("你好，python")    #输出：你好，python


#  调用函数
say_hello()


#############                        带参数的函数

def add(a,b):
    print(a+b)  # 调用函数

add(6,7)  # 输出 13


############                            带返回值return

def get_sum(a, b):
    return a + b  # 返回结果

result = get_sum(2, 4)
print(result)  # 输出：6


##############                          函数求阶乘

# 函数：求 n 的阶乘
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print(factorial(5))  # 输出：120


###############                         函数判断素数

# 函数：判断是否为素数
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return False
    return True

print(is_prime(7))   # 输出：True
print(is_prime(10))  # 输出：False


################                        函数批量判断素数

def show_prime(start,end):
    for n in range(start,end+1):
        if is_prime(n):
            print(n,end=" ")
     # 输出：2 3 5 7 11 13 17 19

show_prime(2,20)
