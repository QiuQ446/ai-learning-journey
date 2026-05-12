"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

图示两个链表在节点 c1 开始相交：

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'

输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB
        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pA



思路：双指针，分别指向两个链表的头节点，逐步向后遍历。
当其中一个指针到达链表末尾时，跳到另一个链表的头节点继续遍历。
这样两个指针会在相交节点相遇，如果没有相交节点，
则会同时到达链表末尾（None），返回 None。        

代码逐行翻译

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 让两个人从各自入口出发
        pA = headA  # 你从A入口出发
        pB = headB  # 你女朋友从B入口出发

        while pA != pB:  # 你们碰面之前，就一直走
            # 你的视角：如果还没逛完，就往前走一步；逛完了，就跳到她的入口重新走
            pA = pA.next if pA else headB
            # 她的视角：如果还没逛完，就往前走一步；逛完了，就跳到你的入口重新走
            pB = pB.next if pB else headA

        # 碰面了：要么在交叉点，要么一起停在None
        return pA

        

"""