"""

用 random.randint(1,100) 生成随机数

while True 接收用户输入

if 判断大了/小了/猜中

猜中后显示一共猜了几次并退出

"""

import random
number = random.randint(1,100)
guess_count = 0

while True:
    guess_number = int(input("请输入你猜的数字(在1~100):"))
    guess_count += 1
    
    if guess_number < number:
        print("太小了！")

    elif guess_number > number:
        print("太大了！")

    else:
        print(f"恭喜你猜中了！你一共猜了{guess_count}次。")
        break
