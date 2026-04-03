class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = dict()
        ans = 0
        l = 0
        for r in range(len(s)):
            if s[r] in curr and curr[s[r]] >= l:
                l = curr[s[r]] + 1
            
            curr[s[r]] = r
            ans = max(ans, r-l+1)
        return ans