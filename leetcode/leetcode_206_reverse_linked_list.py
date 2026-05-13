"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
 

示例 1：


输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：


输入：head = [1,2]
输出：[2,1]
示例 3：

输入：head = []
输出：[]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next   # 1. 存下家
            curr.next = prev        # 2. 箭头反转
            prev = curr             # 3. 三人前移
            curr = next_temp
        
        return prev  # prev 就是新链表的头


🧠 思路
反转链表就是把所有节点的指针方向倒过来。想象你手里有三张牌，依次往后移动，每次都把中间那张牌的箭头反过来指向前一张。

你需要三个指针：

prev：已经反转好的前一个节点（初始为 None，因为反转后原头节点会指向空）

curr：当前正在处理的节点

next_temp：临时保存下一个节点（因为反转指针后，你就找不到原来的下一站了）

每一步做三件事：

先把下一站存好（next_temp = curr.next）

把当前节点的箭头反过来（curr.next = prev）

三人整体往后移一步（prev = curr, curr = next_temp）




"""