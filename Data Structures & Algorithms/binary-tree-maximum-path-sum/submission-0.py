# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # each node can be treated as a potential peak (apex). 
        # a path through a node can extend to its left/right child, but a path going up to a parent can only pick one branch to maintain
        max_sum = float('-inf')

        def max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0
            
            left_gain = max(0, max_gain(node.left))
            right_gain = max(0, max_gain(node.right))

            current_max_path = node.val + left_gain + right_gain

            max_sum = max(max_sum, current_max_path)

            return node.val + max(left_gain, right_gain)
        max_gain(root)
        return max_sum