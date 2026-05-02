"""
创建列表：建一个自己的“梦想汽车”列表，打印每个元素

增：用 append 加一辆车，用 insert 在指定位置插一辆

删：用 del 删除指定位置、用 pop 弹出末尾、用 remove 根据值删除

改：直接通过索引修改某个元素

排序：用 sort() 和 sorted() 排序，reverse() 反转

长度：用 len() 获取列表长度

"""

dream_cars = ["特斯拉", "法拉利", "兰博基尼"]

for car in dream_cars:
    print(car)

dream_cars.append("宝马")
dream_cars.insert(0,"奔驰")
print(dream_cars)


dream_cars.append("奥迪")
del dream_cars[1]
print(dream_cars)


last_car = dream_cars.pop()
print(last_car)
print(dream_cars)


dream_cars.remove("法拉利")
print(dream_cars)

dream_cars[1] = "保时捷"
print(dream_cars)



nums = [3,2,4,5,4,3,2,5,6,7,8]

nums.sort()
print(nums)

sorted_nums = sorted(nums)
print(sorted_nums)

nums.reverse()
print(nums)


print(len(nums))
