# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # head = 1,2,3,4,5
        # expect = 1,5,2,4,3
        # split at the midpoint
        #   use fast/slow
        # reverse the second half
        #   reverse 4->5 to 5->4->None
        # interleave nodes
        if not head or not head.next:
            return

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # when fast end, slow will be end of first half
        second = slow.next
        slow.next = None # break original to two half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        