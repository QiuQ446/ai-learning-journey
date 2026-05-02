"""
切片：list[起始:结束:步长]

创建一个数字列表 nums = [10,20,30,40,50,60]

取出前3个、后3个、每隔一个取一个、整个列表的副本 [:]

理解切片返回的是新列表，原列表不变
"""

nums = [10, 20, 30, 40, 50, 60]

#取出前3个元素
first_three = nums[:3]
print(first_three)

#取出后3个元素
last_three = nums[-3:]
print(last_three)

#每隔一个取一个元素
every_other = nums[::2]
print(every_other)

#整个列表的副本
copy_of_nums = nums[:]
print(copy_of_nums)
print(nums)  # 验证原列表未被修改


"""
列表推导式（让你写出更 Pythonic 的代码）

生成 1-10 的平方数列表：[x**2 for x in range(1,11)]

从 ["apple", "banana", "cat", "dog"] 筛选出长度大于3的单词

把刚才的 for 循环生成平方数改成列表推导式写一遍
"""


squares1 = [x**2 for x in range(1, 11)]
print(squares1)


#生产一个列表，包含1-10的数字的两倍

squares2 = [x*2 for x in range(1, 11)]
print(squares2)


words = ["apple", "banana", "cat", "dog"]
long_words = [word for word in words if len(word) > 3]
print(long_words)


#把刚才的 for 循环生成平方数改成列表推导式写一遍

squares3 = []
for x in range(1, 11):  
    squares3.append(x**2)
print(squares3)