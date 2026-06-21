"""
异步编程入门 —— async/await
"""
import asyncio
import time

# ===== 1. 同步版本：一个做完才做下一个 =====
def make_tea():
    print("🍵 开始泡茶...")
    time.sleep(2)  # 模拟等待 2 秒
    print("🍵 茶泡好了！")
    return "茶"

def make_coffee():
    print("☕ 开始冲咖啡...")
    time.sleep(2)  # 模拟等待 2 秒
    print("☕ 咖啡冲好了！")
    return "咖啡"

print("=" * 30)
print("同步版：一个做完才做下一个")
print("=" * 30)
start = time.time()
make_tea()
make_coffee()
print(f"总耗时：{time.time() - start:.1f} 秒")
print()

# ===== 2. 异步版本：同时做 =====
async def make_tea_async():
    print("🍵 开始泡茶...")
    await asyncio.sleep(2)  # await = "我去干别的，好了叫我"
    print("🍵 茶泡好了！")
    return "茶"

async def make_coffee_async():
    print("☕ 开始冲咖啡...")
    await asyncio.sleep(2)  # await = "我去干别的，好了叫我"
    print("☕ 咖啡冲好了！")
    return "咖啡"

async def main():
    print("=" * 30)
    print("异步版：同时做")
    print("=" * 30)
    start = time.time()
    # 同时启动两个任务！
    await asyncio.gather(
        make_tea_async(),
        make_coffee_async()
    )
    print(f"总耗时：{time.time() - start:.1f} 秒")

asyncio.run(main())