# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # we can use preorder DFS 
        if not root:
            return "N"
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                res.append("N")
                continue
            
            res.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)

        return ",".join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "N":
            return None
        
        vals = data.split(",")
        root = TreeNode(int(vals[0]))

        stack = [[root, 0]]

        for val in vals[1:]:
            parent, state = stack[-1]

            if val != "N":
                child = TreeNode(int(val))
                if state == 0:
                    parent.left = child
                    stack[-1][1] = 1
                else:
                    parent.right = child
                    stack.pop()
                stack.append([child, 0])
            else:
                if state == 0:
                    stack[-1][1] = 1
                else:
                    stack.pop()
        
        return root
                

