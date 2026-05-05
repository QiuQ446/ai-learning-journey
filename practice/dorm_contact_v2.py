"""
def add_contact(contacts_dict): 把新增逻辑独立出来，把字典传进去。

def search_contact(contacts_dict): 接收字典，实现模糊查找或精确查找。

def show_all(contacts_dict): 接收字典，格式化打印全部成员。

def main(): 做一个无限循环菜单，根据用户输入调用不同函数


"""

def add_contact(contacts_dict):
    name = input("请输入姓名：")
    phone = input("请输入电话号码：")
    contacts_dict[name] = phone
    print(f"已添加联系人：{name} - {phone}")

def search_contact(contacts_dict):
    name = input("请输入要查找的姓名：")
    if name in contacts_dict:
        print(f"找到联系人：{name} - {contacts_dict[name]}")
    else:
        print("未找到该联系人。")

def show_all(contacts_dict):
    if not contacts_dict:
        print("联系人列表为空。")
    else:
        print("所有联系人：")
        for name, phone in contacts_dict.items():
            print(f"  {name} - {phone}")

def main():
    contacts = {}
    while True:
        print("\n--- 宿舍联系人管理 ---")
        print("1. 添加联系人")
        print("2. 查找联系人")
        print("3. 显示所有联系人")
        print("4. 退出")
        
        choice = input("请选择操作：")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            show_all(contacts)
        elif choice == "4":
            print("感谢使用！")
            break
        else:
            print("无效选择，请重新输入。")

if __name__ == "__main__":
    main()