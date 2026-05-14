"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1：

输入：nums = [3,2,3]
输出：3
示例 2：

输入：nums = [2,2,1,1,1,2,2]
输出：2

🧠 思路
给你一个数组，里面有一个数字出现次数超过数组长度的一半，找出这个数字。

最省事的方法（用字典）：遍历数组，用字典统计每个数字出现的次数。
哪个数字出现次数超过 len(nums) // 2，就直接返回它。

harsh表思想
"""
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = {}
#         half = len(nums) // 2
#         for num in nums:
#             count[num] = count.get(num, 0) + 1
#             if count[num] > half:
#                 return num
