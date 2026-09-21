# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # post order travasel, 
        # leaf node 2:
        #   both left/right are None, max depth is 1 + max(0, 0) = 1
        # leaf node 4:
        #   smae, max depth 1+max(0,0)=1
        # leaf node 3:
        #   left subtree returns 1, righ=0
        #   max depth 1+max(1,0)=2
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1+max(left_depth, right_depth)