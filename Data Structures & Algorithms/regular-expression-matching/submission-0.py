class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # i and j pointer, branching whenever a * appears
        # dp[i][j] means if we can match s[:i] using p[:j]
        # j==n -> pattern exhausted
        # if pattern exhausted and entire input string matches -> dp[m][n]=True
        m, n = len(s), len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n-1, -1, -1):
                match = i<m and (s[i]==p[j] or p[j]==".")
                if j+1<n and p[j+1]=="*":
                    dp[i][j] = dp[i][j+2] or (match and dp[i+1][j])
                elif match:
                    dp[i][j] = dp[i+1][j+1]
        return dp[0][0]