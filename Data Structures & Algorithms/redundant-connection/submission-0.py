class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [1] * (n+1)

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(u: int, v: int) -> bool:
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return False
            
            if rank[root_u] >= rank[root_v]:
                parent[root_v] = root_u
                rank[root_u] += rank[root_v]
            else:
                parent[root_u] = root_v
                rank[root_v] += rank[root_u]
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
        return []