"""
json.dump(obj, f) — 把字典/列表存成JSON文件

json.load(f) — 把JSON文件读回成Python对象

实战：建一个学生字典 {"name": "邱权", "skills": ["Python", "Git"]}，
存成 student.json，再读出来打印
"""

# 必须先导入 json 模块（Python 内置，无需安装）
import json

# 1. 定义要保存的 Python 字典数据
student = {
    "name": "邱权",
    "skills": ["Python", "Git"]
}

# ========== 2. JSON 写入文件（存数据） ==========
# w = 写入模式，utf-8 防止中文乱码
# json.dump(要保存的对象, 文件对象)
with open("student.json", "w", encoding="utf-8") as f:
    # ensure_ascii=False 让中文正常显示，不变成 Unicode 编码
    json.dump(student, f, ensure_ascii=False, indent=4)

print("✅ 数据已成功保存到 student.json 文件")

# ========== 3. JSON 读取文件（取数据） ==========
# r = 只读模式
# json.load(文件对象) → 自动转回 Python 字典/列表
with open("student.json", "r", encoding="utf-8") as f:
    # 读出来直接就是 Python 字典
    loaded_student = json.load(f)

# ========== 4. 打印读取结果 ==========
print("\n===== 从 JSON 文件读取的数据 =====")
print(loaded_student)
print("姓名：", loaded_student["name"])
print("技能：", loaded_student["skills"])


'''
json.dump(数据, 文件对象)	    
        把 Python 字典 / 列表 写入 JSON 文件（存盘）
json.load(文件对象)	        
        把 JSON 文件读回 Python 字典 / 列表(读取)


ensure_ascii=False：让中文正常显示，不变成乱码
indent=4：让 JSON 文件自动格式化、换行缩进，打开文件看得更清楚
encoding="utf-8"：彻底解决中文乱码       
'''