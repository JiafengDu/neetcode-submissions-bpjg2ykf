# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_tail = dummy #prev tail should point to new head after reverse
            
        while True:
            tail = prev_tail
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            group_head = prev_tail.next
            next_head = tail.next
            #prev_tail.next = tail
            #next_head = tail.next
            
            prev = next_head
            curr = group_head
            # now we have curr to tail, curr.next should be prev
            while curr!=next_head:
                temp = curr.next # original next node
                curr.next = prev
                prev = curr
                curr = temp
            
            prev_tail.next = tail
            prev_tail = group_head
        return dummy.next

        