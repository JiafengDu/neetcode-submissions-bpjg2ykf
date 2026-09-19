# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node of the result, set curr and carry
        # loop while l1, l2, carry is non-zero
        #   extract digit from l1, l2
        #   copute total = l1.val+l2.val+carry
        #   update carry
        #   create a new node 
        #   advance curr as well as l1,l2
        # return dummy.next

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 
            
            total = v1+v2+carry
            carry = total // 10
            curr.next = ListNode(total % 10)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next