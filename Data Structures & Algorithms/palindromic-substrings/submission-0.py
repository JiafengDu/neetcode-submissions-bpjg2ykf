class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left: int, right: int):
            res = 0
            while left >= 0 and right < len(s) and s[left]==s[right]:
                left -= 1
                right += 1
                res += 1
            return res
        total = 0
        for i in range(len(s)):
            # odd
            total += expand(i, i)
            # even
            total += expand(i, i+1)
        return total