class Solution:
    def numDistinct(self, s: str, t: str) -> int:
         # index i for s, index j for t
         # if s[i]!=t[j] -> skip i
         # else:
         #  -> use s[i]
         #  -> skip s[i]
         #  -> dp[i][j] = sum(dp[i+1][j+1], dp[i+1, j])
         # base case:
         #  -> j reach end, 1 valid subsequence
         #  -> i reach end but j don't, 0 valid
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        
        return dp[m][n]