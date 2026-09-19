"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        # pass 1: create a clone of each node and insert it right next to the original
        curr = head
        while curr:
            copy = Node(curr.val, curr.next)
            curr.next = copy
            curr = copy.next
        
        # pass 2: connect the random pointers for the copied nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # pass 3: separate two lists to restore original and copy
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = curr.next.next
            copy.next = copy.next.next if copy.next else None
            curr = curr.next

        return copy_head