"""
append() 在末尾加一个

insert(索引, 元素) 插入到指定位置

del list[索引] 删除指定位置

# 最后打印整个列表
print("我的梦想车列表：", dream_cars)

list[索引] = 新值 修改元素
"""





list1 = ["海贼王","全职猎人","全能百分百"]

print(list1[0])

# 创建一个空列表 dream_cars
dream_cars = []

# 用 append 依次加入三辆梦想中的车
dream_cars.append("Tesla Model S")
dream_cars.append("Lamborghini Huracan")
dream_cars.append("Porsche 911")

# 打印"我想拥有一辆XXX"
for car in dream_cars:
    print(f"我想拥有一辆{car}")

# 最后打印整个列表
print("我的梦想车列表：", dream_cars)  
#输出列表中的第一个元素


print(list1[-1])  
#输出列表中的最后一个元素


list1.append("火影忍者")  
#在列表末尾添加一个元素（火影忍者）
print(list1)  
#输出修改后的列表


list1.insert(1,"死神") 
#在列表的第二个位置插入一个元素（死神）
print(list1)  
#输出修改后的列表（在海贼王和全职猎人之间多一个死神）


del list1[2]  
#删除列表中的第三个元素（全职猎人）
print(list1)  
#输出修改后的列表（全职猎人被删除了）


r1 = list1.pop()
#删除列表中的最后一个元素（火影忍者）并返回该元素
print(r1)
print(list1)
#输出修改后的列表（火影忍者被删除了）


r2 = list1.pop(1)
#删除列表中第二个元素（死神）并返回该元素
print(r2)
print(list1)
#输出修改后的列表（死神被删除了）


list1.remove("海贼王")
#根据值删除列表中的元素（海贼王）
print(list1)


list1[0] = "十万个冷笑话"
#修改列表中的第一个元素为十万个冷笑话
print(list1)












"""

sort() 永久排序 vs sorted() 临时排序

reverse() 反转

len() 获取长度

"""

list2 = [3, 1, 4, 1, 5, 9]

list2.sort()
#永久排序，修改了原列表
print(list2)



list3 = [3, 1, 4, 1, 5, 9]
sorted_list3 = sorted(list3)
#临时排序，返回一个新的列表，原列表不变
print(sorted_list3)
print(list3)

list2.reverse()
#反转列表
print(list2)


list4 = [4, 2, 9, 4, 7]

list4.sort(reverse=True)
#永久排序，降序排列
print(list4)

list5 = [3, 2, 9, 4, 7]
sorted_list5 = sorted(list5,reverse=True)
#临时排序，返回一个新的列表，降序排列
print(sorted_list5)
print(list5)


list6 = [1, 2, 3, 4, 5]
length = len(list6)
#获取列表的长度
print(length)
#输出列表的长度5

"""
Testing the list operations

question: 创建一个空列表 
dream_cars，然后用 append 依次加入三辆你梦想中的车，打印"我想拥有一辆XXX"，最后打印整个列表
"""

dream_cars = []
dream_cars.append("特斯拉")
dream_cars.append("法拉利")
dream_cars.append("兰博基尼")
print(dream_cars)
