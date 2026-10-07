class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = {}
        for word in wordDict:
            curr = root
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr["$"] = True
        
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            curr = root
            for j in range(i, n):
                char = s[j]
                if char not in curr:
                    break
                curr = curr[char]
                if curr.get("$"):
                    dp[j+1] = True
        
        return dp[n]