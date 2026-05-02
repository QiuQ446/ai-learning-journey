"""

条件测试：写10个 ==, !=, >, <, in, not in 的测试，每个打印“预测为真/假”

if-elif-else：写一个给年龄分级的程序（<2婴儿，2-4幼儿，4-13儿童，13-20青少年，20-65成年人，>65老年人）

结合列表：建一个“当前在线用户”列表，再建一个“已注册用户”列表。遍历注册用户，打印“XXX在线”或“XXX已注册但未在线”，用一个 if 判断 user in online_users 即可

判空：用 if list: 检查空列表，给用户友好提示

"""
# 1. == 测试：预测为真
print("5 == 5 预测为真，实际结果：", 5 == 5)
# 2. == 测试：预测为假
print("3 == 4 预测为假，实际结果：", 3 == 4)

# 3. != 测试：预测为真
print("'apple' != 'orange' 预测为真，实际结果：", 'apple' != 'orange')
# 4. != 测试：预测为假
print("10 != 10 预测为假，实际结果：", 10 != 10)

# 5. > 测试：预测为真
print("7 > 3 预测为真，实际结果：", 7 > 3)
# 6. < 测试：预测为真
print("2 < 9 预测为真，实际结果：", 2 < 9)

# 7. in 测试：预测为真
print("'a' in 'apple' 预测为真，实际结果：", 'a' in 'apple')
# 8. in 测试：预测为假
print("'z' in 'banana' 预测为假，实际结果：", 'z' in 'banana')

# 9. not in 测试：预测为真
print("'x' not in [1, 2, 3] 预测为真，实际结果：", 'x' not in [1, 2, 3])
# 10. not in 测试：预测为假
print("'python' not in 'I love python' 预测为假，实际结果：", 'python' not in 'I love python')



age = 25
if age < 2:
    print("婴儿")   
elif age < 4:
    print("幼儿")
elif age < 13:
    print("儿童")
elif age < 20:  
    print("青少年")
elif age < 65:
    print("成年人")
else:
    print("老年人")



online_users = ['alice', 'bob', 'charlie']
registered_users = ['alice', 'bob', 'charlie', 'dave', 'eve']
for user in registered_users:
    if user in online_users:
        print(f"{user}在线")
    else:
        print(f"{user}已注册但未在线")

empty_list = []
if empty_list:
    print("列表不为空")
else:
    print("列表为空")