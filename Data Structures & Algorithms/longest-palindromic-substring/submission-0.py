class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        start = 0
        max_len = 1
        
        def expand(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            curr_len = right-left-1
            return curr_len, left+1
        
        for i in range(len(s)-1):
            odd_len, odd_start = expand(i, i)
            if odd_len > max_len:
                max_len = odd_len
                start = odd_start
            even_len, even_start = expand(i, i+1)
            if even_len > max_len:
                max_len = even_len
                start = even_start
        return s[start:start+max_len]
