class DSU:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0]*size
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x:int, y:int) -> None:
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = self.parent[root_y]
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        positions = [None] * (n*n)
        for r in range(n):
            for c in range(n):
                positions[grid[r][c]] = (r, c)

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        dsu = DSU(n*n)
        start_node = 0
        end_node = n*n-1

        for t in range(n*n):
            r, c = positions[t]
            curr_id = r*n + c

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<n and 0<=nc<n and grid[nr][nc] <= t:
                    neighbor_id = nr*n + nc
                    dsu.union(curr_id, neighbor_id)

            if dsu.find(start_node) == dsu.find(end_node):
                return t
        return 0