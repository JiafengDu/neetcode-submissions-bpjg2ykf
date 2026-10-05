class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree:
        #   fully connected - every node can reach every other node
        #   acyclic - no loop
        # a tree of n nodes - it must contain exactly n-1 edges

        if len(edges) != n-1:
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        def dfs(node: int, parent: int) -> bool:
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent: 
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        
        return len(visited) == n