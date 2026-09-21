# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative in-order DFS
        # traverse as far left as possible, pushing each node onto the stack
        # pop a node from the stack and decrement k
        # if k=0, the current node is the answer
        # move to the right child of the current node and repeat until k = 0
        stack = []
        curr = root
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            
            curr = curr.right
        