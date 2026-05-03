"""
字典是键值对的数据容器，格式：{键: 值, 键: 值}

键 (key)：不可变（字符串、数字、元组），唯一不能重复
值 (value)：任意类型（数字、字符串、列表、字典都可以）
无序、可修改

"""
"""
                            创建字典
"""


#方式1 ：大括号直接创建

dict1 = {"name": "Alice", "age": 30, "city": "New York"}


#方式2：使用 dict() 函数创建

dict2 = dict(name="Bob", age=25, city="Los Angeles")

print(dict1)
print(dict2)    

#空字典

dict3 = {}

dict4 = dict()


print(dict3)
print(dict4)



"""                          
                                 访问字典元素

"""

stu = {"name":"david","age":30,"score":90}

#访问字典元素：通过键访问对应的值

print(stu["name"])  # 输出: david
print(stu["age"])   # 输出: 30
print(stu["score"]) # 输出: 90

#使用 get() 方法访问字典元素：如果键不存在，不会报错，返回 None 或指定的默认值

print(stu.get("name"))
print(stu.get("age"))
print(stu.get("score"))


print(stu.get("gender"))  # 输出: None  


"""

                                 增、改、删内容

"""


dict5 = {"name":"jom"}

#键存在就是修改，不存在就是新增

dict5["age"] = 18 # 新增键值对
dict5["name"] = "tom" # 修改键值对

print(dict5)  # 输出: {'name': 'tom', 'age': 18}


#删除键值对：使用 del 语句或 pop() 方法

del dict5["age"]  # 删除键 'age' 和对应的值
print(dict5)  # 输出: {'name': 'tom'}

dict5.pop("name")  # 删除键 'name' 和对应的值
print(dict5)  # 输出: {}

dict5.clear()  # 删除字典中所有的键值对,清空整个字典



"""
                                    常用获取内容方法
"""

dict6 = {"a":1,"b":2,"c":3}

#获取所有键：keys() 方法返回一个包含字典所有键的视图对象
print(dict6.keys())  # 输出: dict_keys(['a', 'b', 'c'])

#获取所有值：values() 方法返回一个包含字典所有值的视图对象
print(dict6.values())  # 输出: dict_values([1, 2, 3])

#获取所有键值对：items() 方法返回一个包含字典所有键值对的视图对象
print(dict6.items())  # 输出: dict_items([('a', 1), ('b', 2), ('c', 3)])


"""
                                    字典的遍历                                    
"""


dict7 = {"x":10,"y":20,"z":30}
#遍历字典的键：使用 for 循环直接遍历字典，默认遍历的是键

for key in dict7:
    print(key)  # 输出: x y z

#遍历字典的值：使用 values() 方法获取所有值进行遍历

for value in dict7.values():
    print(value)  # 输出: 10 20 30

#遍历字典的键值对：使用 items() 方法获取所有键值对进行遍历

for key, value in dict7.items():
    print(f"键: {key}, 值: {value}")# 输出:    键: x, 值: 10
                                            # 键: y, 值: 20
                                            # 键: z, 值: 30