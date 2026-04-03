class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[m-1][n-1] = 1
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                for delta_r, delta_c in [(1,0), (0, 1)]:
                    future_r, future_c = row+delta_r, col+delta_c
                    futurePaths = 0 if (future_r >= m or future_c >= n) else dp[future_r][future_c]
                    dp[row][col] += futurePaths
        return dp[0][0]