"""
打造一个功能完备的“学生成绩管理系统”，用JSON文件持久化数据，支持增删改查。
"""

#------------------- 数据层——加载与保存 ------------------
import json  # 导入JSON模块
import os    # 导入os模块，用于检查文件是否存在

# 定义文件名常量
DATA_FILE = "Student_Scores.json"

def load_data():
    """从JSON文件加载数据,文件不存在就返回空字典"""
    if not os.path.exists(DATA_FILE):
        return {}  # 文件不存在，返回空字典
    try:
        with open(DATA_FILE, "r", encoding="UTF-8")as f:
            return json.load(f)  # 读回Python字典
    except json.JSONDecodeError:
        print("数据文件损坏，无法解析。请检查文件内容。")
        return {}  # 解析失败，返回空字典
    
def save_data(data):
    """把数据保存到JSON文件"""
    with open(DATA_FILE, "w", encoding="UTF-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)  # 美化JSON文件


#------------------- 业务层——增删改查功能 ------------------
def add_student(data):
    """添加学生成绩"""
    name = input("请输入学生姓名：")
    if name in data:
        print(f"错误：学生 {name} 已存在。")
        return
    try:
        score = float(input("请输入学生成绩："))
    except ValueError:
        print("错误：请输入有效的数字成绩。")
        return
    data[name] = score
    save_data(data)
    print(f"成功:已添加{name},成绩：{score}")


def query_student(data):
    """查询学生成绩"""
    name = input("请输入要查询的学生姓名：")
    score = data.get(name)
    if score is not None:
        print(f"{name} 的成绩是：{score}")
    else:
        print(f"系统中没有 '{name}' 的记录。")

def delete_student(data):
    """删除学生成绩"""
    name = input("请输入要删除的学生姓名：")
    if name in data:
        del data[name]
        save_data(data)
        print(f"成功:已删除{name}的记录。")
    else:
        print(f"系统中没有 '{name}' 的记录。")

def list_all_students(data):
    if not data:
        print("系统中暂无记录。")
        return
    print("\n--- 学生成绩列表 ---")
    for name, score in data.items():
        print(f"{name}: {score}")
    print("--------------------\n")

#------------------- 交互层——菜单主循环 ------------------
def main():
    data = load_data()  # 启动时加载数据
    print("欢迎使用学生成绩管理系统！")
    
    while True:
        print("\n请选择操作：")
        print("1. 添加学生成绩")
        print("2. 查询学生成绩")
        print("3. 删除学生记录")
        print("4. 列出所有学生成绩")
        print("5. 退出系统")
        
        choice = input("请输入选项编号：")
        
        if choice == "1":
            add_student(data)
        elif choice == "2":
            query_student(data)
        elif choice == "3":
            delete_student(data)
        elif choice == "4":
            list_all_students(data)
        elif choice == "5":
            print("感谢使用，再见！")
            break
        else:
            print("无效选项，请重新输入。")

if __name__ == "__main__":
    main()