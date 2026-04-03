class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        m = len(grid)
        n = len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    queue.append((row, col))
        
        while queue:
            for _ in range(len(queue)):
                dRow, dCol = queue.popleft()
                neiDis = grid[dRow][dCol] + 1
                for deltaM, deltaN in [(1,0), (-1,0), (0,1), (0,-1)]:
                    neiM = dRow+deltaM
                    neiN = dCol+deltaN
                    if neiM>=0 and neiM<m and neiN>=0 and neiN<n:
                        if grid[neiM][neiN] > neiDis:
                            grid[neiM][neiN] = neiDis
                            queue.append((neiM, neiN))
        