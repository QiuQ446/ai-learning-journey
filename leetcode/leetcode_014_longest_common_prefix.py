"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
"""
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # 削掉最后一个字符
                if not prefix:
                    return ""
        return prefix
    
"""

"""
startswith()：判断字符串是不是以指定前缀开头



s = "hello world"

# 判断是不是 hello 开头
print(s.startswith("hello"))  
# 输出 True

print(s.startswith("hi"))     
# 输出 False



s = "hello world"
# 从下标6开始判断
print(s.startswith("world", 6)) 
# True



"""