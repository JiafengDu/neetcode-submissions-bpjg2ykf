# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        sz = 0
        curr = head
        while curr:
            curr = curr.next
            sz += 1
        target = sz-n
        curr = dummy
        # [0,1,2]
        while target >= 0:
            prev = curr #prev is 0
            curr = curr.next
            target -= 1
            # curr become 1
        prev.next = curr.next
        return dummy.next

