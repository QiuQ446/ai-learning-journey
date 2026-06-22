"""
pytest 入门 —— 测试简单的函数
"""

# ===== 被测试的函数 =====
def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0


# ===== 测试函数（名字必须以 test_ 开头）=====
def test_add():
    assert add(1, 2) == 3       # 断言：我坚信 1+2=3
    assert add(-1, 5) == 4      # 断言：我坚信 -1+5=4
    assert add(0, 0) == 0       # 断言：我坚信 0+0=0

def test_is_even():
    assert is_even(2) == True   # 2 是偶数
    assert is_even(3) == False  # 3 不是偶数
    assert is_even(0) == True   # 0 是偶数