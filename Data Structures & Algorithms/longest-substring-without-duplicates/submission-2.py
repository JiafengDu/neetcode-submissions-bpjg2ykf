class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        longest = 0
        l, r = 0, 0
        while r < len(s):
            count[s[r]] += 1
            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
            r += 1
        return longest
