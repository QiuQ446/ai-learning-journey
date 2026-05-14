"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # 虚拟头节点
        curr = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # 把剩下的那个链表直接接上
        curr.next = list1 if list1 else list2
        
        return dummy.next


    核心逻辑：创建一个虚拟头节点 dummy，然后用一个指针 curr 指向它。同时遍历两个链表，每次比较两个链表的当前节点，把较小的那个接到 curr 后面，然后移动对应的指针。最后把剩下的那个链表直接接上。

就像两摞已经排好序的扑克牌，你每次从两摞最上面选较小的那张，放到新的一摞上。    



"""