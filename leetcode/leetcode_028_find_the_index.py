"""
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。

 

示例 1：

输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
示例 2：

输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
 
"""

"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 如果 needle 是空字符串，直接返回 0
        if not needle:
            return 0
        
        # 遍历 haystack，到剩余长度不够 needle 长度时停止
        for i in range(len(haystack)-len(needle)+1):
            r = haystack[i:len(needle)+i]
            if r == needle:
                return i
        return -1


        核心思路
 从 haystack 的第一个字符开始，逐个检查以当前位置开头的子串是否等于 needle

range(len(haystack) - len(needle) + 1) 保证剩余字符数不够匹配时自动停止

如果用 Python 内置方法，一行就可以搞定：return haystack.find(needle)——但面试一般会让你手写循环
        """