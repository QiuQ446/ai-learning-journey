'''
写文件：用 with open("test.txt", "w", encoding="utf-8") as f: 写几行字

读文件：用 with open("test.txt", "r", encoding="utf-8") as f: 读出来并打印

追加写入：用 "a" 模式往文件末尾加新内容

理解：with 语句自动关闭文件，encoding="utf-8" 避免中文乱码

'''

# ========== 1. 写入文件（w模式：覆盖写入） ==========
# with语句：自动管理文件，用完自动关闭，无需手动写f.close()
# encoding="utf-8"：强制使用UTF-8编码，解决中文乱码问题

with open("test.txt", "w", encoding="utf-8") as f:
    # write() 写入内容，\n 表示换行
    f.write("这是第一行文字\n")
    f.write("Python文件读写练习\n")
    f.write("Hello, World!\n")

# ========== 2. 读取文件（r模式：只读模式） ==========
with open("test.txt", "r", encoding="utf-8") as f:
    # read() 一次性读取文件全部内容
    content = f.read()
    print("===== 文件读取结果 =====")
    print(content)

# ========== 3. 追加写入（a模式：在文件末尾添加内容） ==========
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("这是追加的第一行内容\n")
    f.write("这是追加的第二行内容\n")

# 再次读取，验证追加效果
with open("test.txt", "r", encoding="utf-8") as f:
    new_content = f.read()
    print("===== 追加后的文件内容 =====")
    print(new_content)