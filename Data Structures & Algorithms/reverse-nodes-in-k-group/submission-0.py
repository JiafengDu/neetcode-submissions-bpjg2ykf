# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # dummy point to head, group_prev = dummy
        # find kth node from group_prev. If kth is None, exit
        # group_next = kth.next
        # iterate curr from group_prev.next to kth, reverse pointers with prev initialize to group_next
        # point group_prev.next to kth
        # move group_prev to the old head of the group, then repeat
        # return dummy.next
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth = self.get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            tail = group_prev.next
            group_prev.next = kth
            group_prev = tail
        return dummy.next
    
    def get_kth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
