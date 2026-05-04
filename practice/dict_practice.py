"""
get() 查一个不存在的键，看它和直接 [] 取值报错的区别。
接着用 for 循环把键值对全打印出来。
"""


dict_own = {"name":"jim","gender":"male","age":25,"favorite_food":"noodles"}

#value1 = dict_own.get("city")
#value2 = dict_own["city"]

#print(value1)  # 输出: None
#print(value2)  # 报错: KeyError: 'city'


for u,v in dict_own.items():
    print(u,v)# 输出:# name jim
                    # gender    male
                    # age   25  
                    # favorite_food noodles

for key in dict_own:
    print(key, dict_own[key]) # 输出:# name jim
                                    # gender    male
                                    # age   25  
                                    # favorite_food noodles


for key in dict_own.keys():
    print(key) 
# 输出:# name
#       # gender
#       # age
#       # favorite_food



for value in dict_own.values():
    print(value)
# 输出:# jim
#       # male
#       # 25
#       # noodles



"""
嵌套

字典里放列表："爱好": ["编程", "打球", "看电影"]

列表里放字典：建 3 个人的名片字典，放进一个列表里，遍历时用 person["姓名"] 取出

"""

person = {"小丽":{"age":18,"gender":"female","hobbies":["编程", "打球", "看电影"]},
          "小红":{"age":20,"gender":"female","hobbies":["阅读", "旅游", "听音乐"]},
          "小强":{"age":22,"gender":"male","hobbies":["游戏", "健身", "看电影"]}
          }

print(person["小丽"]["hobbies"])  # 输出: ['编程', '打球', '看电影']    

print(person["小红"])   # 输出: {'age': 20, 'gender': 'female', 'hobbies': ['阅读', '旅游', '听音乐']}  


for name, info in person.items():
    print(f"姓名: {name}")
    print(f"年龄: {info['age']}")
    print(f"性别: {info['gender']}")
    print(f"爱好: {info['hobbies']}")













