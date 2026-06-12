"""
题目：函数基本功 6 道题

要求：每道题写成一个函数，函数写完立刻调用验证
"""

# 1. 写一个函数 max_of_three(a, b, c)，返回三个数中的最大值
#    不要用内置 max()，自己用 if 判断

# 2. 写一个函数 is_palindrome(s)，判断字符串是否是回文
#    "abcba" → True   "hello" → False
#    （回文就是正着读反着读一样）

# 3. 写一个函数 count_words(s)，统计一个英文句子中每个单词的出现次数
#    返回字典 {"hello": 2, "world": 1, ...}
#    提示：用 s.split() 把句子拆成单词列表

# 4. 写一个函数 filter_even(numbers)，传入一个数字列表，返回只包含偶数的列表
#    用列表推导式一行搞定

# 5. 写一个函数 grade_to_gpa(grade)，输入等级（优秀/良好/中等/及格/不及格）
#    返回对应的 GPA（4.0/3.0/2.0/1.0/0.0）
#    用字典映射，不要用 if-elif

# 6. 写一个函数 make_multiplier(n)，返回一个新函数
#    这个新函数接收一个参数 x，返回 x * n
#    示例：double = make_multiplier(2); double(5) → 10
#    这是"闭包"，不理解没关系，先照猫画虎写出来


1.
def max_of_three(a,b,c):
    if a > b:
        if a >= c:
            return a
        else:
            return c
    if a <= b:
        if b >= c:
            return b
        else:
            return c
print(max_of_three(2,5,1)) #输出 5

2.
def is_palindrome(s):
    s_palindrome = s[::-1]
    if s_palindrome == s:
        return True
    else:
        return False
print(is_palindrome("abcba")) #输出True

3.
def count_words(s):
    word_list = s.split( )
    count_words = {}
    for s in word_list:
        count_words[s] = 0 
    for s in word_list:
        if s in count_words:
            count_words[s] += 1
    return count_words
   
print(count_words("hello hello world"))    #输出{'hello': 2, 'world': 1}

4.
def filter_even(numbers):
    return [i for i in numbers if i % 2 ==0]
print(filter_even([1,2,3,4,5]))

5.
def grade_to_gpa(grade):
    GPA = {"优秀":4.0,"良好":3.0,"中等":2.0,"及格":1.0,"不及格":0.0}
    return GPA[grade]
print(grade_to_gpa("及格"))

6.
def make_multiplier(n):
    def inner(x):
        return x*n
    return inner
double = make_multiplier(2)
print(double(4))