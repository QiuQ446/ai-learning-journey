"""           原代码
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

"""

"""

def generate_number(): 负责生成随机数并返回。

def get_user_guess(): 负责接收用户输入，处理好类型转换（防报错），返回猜测值。

def check_guess(guess, answer): 把判断逻辑封装起来，返回“大了”、“小了”或“猜中了”。

主程序：只负责调用它们，把游戏流程串联起来。

"""

def generate_number():
    import random
    return random.randint(1,100)

def get_user_guess():
    while True:
        try:
            guess = int(input("请输入你猜的数字(在1~100):"))
            return guess
        except ValueError:
            print("请输入一个有效的整数！")

def check_guess(guess, answer):
    if guess < answer:
        return "太小了！"
    elif guess > answer:
        return "太大了！"
    else:
        return "猜中了！"
    

def main():
    number = generate_number()
    guess_count = 0
    
    while True:
        guess = get_user_guess()
        guess_count += 1
        
        result = check_guess(guess, number)
        print(result)
        
        if result == "猜中了！":
            print(f"恭喜你猜中了！你一共猜了{guess_count}次。")
            break

if __name__ == "__main__":
    main()