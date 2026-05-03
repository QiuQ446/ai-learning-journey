"""
                             宿舍通讯录


        实现：

输入室友名字 → 打印他的全部信息

输入室友名字 + 信息类型（如“电话”） → 打印对应信息

如果查无此人，用 get() 友好提示
"""

contacts = {
    "小卢":{"电话":2143245322,"年龄":20,"性别":"男","爱好":["编程","打球","看电影"]},
    "小严":{"电话":2143245323,"年龄":19,"性别":"男","爱好":["阅读","旅游","听音乐"]},
    "小关":{"电话":2143245324,"年龄":19,"性别":"男","爱好":["游戏","健身","看电影"]}
}

name = input("请输入室友名字：")

if name in contacts:
    info_type = input("请输入信息类型（如“电话”）：")
    info = contacts[name].get(info_type)
    
    if info is not None:
        print(f"{name}的{info_type}是：{info}")
    else:
        print(f"{name}没有{info_type}的信息。")
else:
    print(f"查无此人：{name}")

