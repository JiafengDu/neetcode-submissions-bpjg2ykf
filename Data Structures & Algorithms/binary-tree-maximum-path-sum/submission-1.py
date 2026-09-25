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
        if not root:
            return 0

        stack = [(root, False)]

        gains = {}
        max_sum = float("-inf")

        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            
            if visited:
                left_gain = max(0, gains.get(node.left, 0))
                right_gain = max(0, gains.get(node.right, 0))

                max_sum = max(max_sum, node.val + left_gain + right_gain)

                gains[node] = node.val + max(left_gain, right_gain)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        return max_sum