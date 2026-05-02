"""
普通遍历：建一个喜欢的食物列表，用 for food in foods: 打印“我喜欢吃XXX”

range() 函数：打印1到20的数字；创建包含1到100万的列表，验证 min/max/sum

列表推导式回顾：用一行代码生成1到10的立方列表，结合刚才学的 for

切片循环：用 for 遍历列表的前三个元素

"""



foods = ["apple", "banana", "cherry"]
for food in foods:
    print(f"我喜欢吃{food}")


for i in range(1,21):
    print(i,end=" ")


numbers = list(range(1,1000001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))


cubes = [x**3 for x in range(1,11)]
print(cubes)




nums = [6,7,4,3,2,5,6,8,7,3,5,6]

lomh_nums = [num for num in nums if num > 6]
print(lomh_nums)

for num in nums[:3]:
    print(num)