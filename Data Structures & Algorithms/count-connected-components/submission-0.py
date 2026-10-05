class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n
        components = n

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
            if union(u, v):
                components -= 1
        return components