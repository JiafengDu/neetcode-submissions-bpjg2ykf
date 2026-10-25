# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        first, second = head, prev
        # 2->4, 8->6
        while second:
            tmp1, tmp2 = first.next, second.next # 6, None
            first.next = second 
            # 4->6
            second.next = tmp1
            # 6->None
            first, second = tmp1, tmp2
            # 6, None
        