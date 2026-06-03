"""
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

 

示例 1 ：

输入：nums = [2,2,1]

输出：1

示例 2 ：

输入：nums = [4,1,2,1,2]

输出：4

示例 3 ：

输入：nums = [1]

输出：1


# 方法一：哈希表
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, freq in count.items():
            if freq == 1:
                return num

# 方法二：异或（更优）
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


方法一（用哈希表）：用你熟悉的字典，统计每个数字出现的次数，
    然后找出次数为 1 的那个。这是 O(n) 时间，O(n) 空间。

方法二（更高级）：用异或运算 ^。两个相同的数异或得 0，
    0 和任何数异或得那个数本身。所以把数组里所有数异或起来，
    结果就是唯一那个数。O(n) 时间，O(1) 空间
        




"""