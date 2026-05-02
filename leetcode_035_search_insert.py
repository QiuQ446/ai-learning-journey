"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

示例 1:

输入: nums = [1,3,5,6], target = 5
输出: 2
示例 2:

输入: nums = [1,3,5,6], target = 2
输出: 1
示例 3:

输入: nums = [1,3,5,6], target = 7
输出: 4

"""

####         常规解法：遍历数组，找到第一个大于等于目标值的位置，返回索引  时间复杂度为 O(n)。

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)
    

"""

基本用法：enumerate(iterable, start=0)，其中 iterable 是需要遍历的对象，start 是索引的起始值，默认为 0。 
2. 返回值：enumerate() 返回一个 enumerate 对象，该对象生成由索引和值组成的元组。每次迭代时，返回一个包含当前索引和对应值的元组。
3. 用法示例：
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"索引: {index}, 值: {fruit}")
输出：
索引: 0, 值: apple
索引: 1, 值: banana
索引: 2, 值: cherry
"""


####        二分查找：在有序数组中，使用二分查找算法来找到目标值的位置或插入位置。时间复杂度为 O(log n)。

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left   # 退出循环时 left 就是插入位置