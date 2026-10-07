class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = True if s[:i] can be segmented
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for word in wordDict:
                if dp[i]:
                    break
                word_len = len(word)
                if i >= len(word) and word==s[i-len(word):i]:
                    dp[i] = dp[i-len(word)]
        print("final dp:", dp)
        return dp[n]