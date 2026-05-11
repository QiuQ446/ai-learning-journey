"""
给你一个链表的头节点 head ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

如果链表中存在环 ，则返回 true 。 否则，返回 false 。

 

示例 1：



输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：



输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：



输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
 

📝 代码实现

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast and fast.next:  # 快指针和它的下一步都存在才继续
            slow = slow.next       # 慢指针走一步
            fast = fast.next.next  # 快指针走两步
            if slow == fast:       # 追上了，有环
                return True
        return False                # 快指针走完了，没环


        ✍️ 核心思路
想象两个人在操场上跑步，一个快（一次两步），一个慢（一次一步）。

如果跑道是环形的，快的人一定会追上慢的人。

如果跑道是直的，快的人会先到终点。

把这个想法搬到链表上：

快指针 fast 每次走两步，慢指针 slow 每次走一步。

如果链表有环，它们必定在环里相遇。

如果链表没环，fast 会先走到尽头（None）。
"""