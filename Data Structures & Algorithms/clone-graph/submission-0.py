"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}

        def dfs(curr_node):
            if curr_node in oldToNew:
                return oldToNew[curr_node]

            copy = Node(curr_node.val)
            oldToNew[curr_node] = copy
            for nei in curr_node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node)