# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node: Optional[TreeNode]) -> List[str]:
            if not node:
                return ["#"]
            return [str(node.val)] + serialize(node.left) + serialize(node.right)
        
        text = serialize(root)
        pattern = serialize(subRoot)

        lps = [0] * len(pattern)
        prev_lps, i = 0, 1
        while i < len(pattern):
            if pattern[i] == pattern[prev_lps]:
                prev_lps += 1
                lps[i] = prev_lps
                i += 1
            else:
                if prev_lps != 0:
                    prev_lps = lps[prev_lps - 1]
                else:
                    lps[i] = 0
                    i += 1
        i = 0
        j = 0

        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
                if j == len(pattern):
                    return True
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return False
                
            


        