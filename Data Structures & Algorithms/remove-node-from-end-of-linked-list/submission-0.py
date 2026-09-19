# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # head is a dummy node
        # right pointer is n steps forward
        # advance boh left, right once at a time until right reaches None
        # remove the left node, so set left.next = left.next.next
        # return dummy.next
        dummy = ListNode(0, head)
        left = dummy
        right = head
        for _ in range(n):
            right = right.next
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next