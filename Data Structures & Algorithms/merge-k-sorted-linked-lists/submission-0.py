# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge two lists until all k lists are merged together
        # edge cases: if lists is empty, return None
        # iterative halving:
        #   step through two lists at a time
        #   merge lists[i] and lists[i+1] using a two-pointer merge helper
        #   collect merged lists and replace the existing lists with the merged set
        # return the single remaining list
        if not lists:
            return None
        while len(lists)>1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merged_lists.append(self.mergeTwoLists(l1, l2))
            lists = merged_lists
        return lists[0]

    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return dummy.next