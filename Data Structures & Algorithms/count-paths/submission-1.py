class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[m-1][n-1] = 1
        directions = [(0,1),(1,0)]
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr>=m or nc>=n:
                        continue
                    dp[r][c] += dp[nr][nc]
        
        return dp[0][0]