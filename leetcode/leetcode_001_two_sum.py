
#暴力法：两层循环，枚举所有的数对，找到和为目标值的数对，返回它们的索引。时间复杂度 O(n^2)，空间复杂度 O(1)。
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count1 = -1
        for i in nums:
            count1 += 1
            count2 = -1
            for j in nums:
                count2 += 1
                if count1 != count2 and i + j == target:
                    return [count1, count2]
        return []
"""


"""
 两数之和：哈希表 O(n) 思路
核心逻辑：遍历数组时，一边走一边往字典里存 {值: 索引}。
对于当前数字 num，算出差值 target - num，去字典里查这个差值在不在。
在的话，直接返回两个索引；不在，就把当前数存进字典继续走。

一遍遍历，时间复杂度 O(n)，空间复杂度 O(n)。

"""

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # 值 → 索引
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

"""

"""
enumerate 函数用于将一个可遍历的数据对象（如列表、元组或字符串）
组合为一个索引序列，同时列出数据和数据下标

"""

#update