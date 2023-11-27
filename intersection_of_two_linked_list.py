# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        fast = headA
        slow = headB
        # fast1=headB
        # slow1=headB
        # while fast!=None:
        while fast != slow:
            fast = fast.next if fast else headB
            slow = slow.next if slow else headA

        return fast
