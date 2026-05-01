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
