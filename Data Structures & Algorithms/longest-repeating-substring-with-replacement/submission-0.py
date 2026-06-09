class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left, right = 0, 0
        freqs = [0]*26
        res = 0
        while right < len(s):
            freqs[ord(s[right])-ord('A')] += 1
            max_freq = max(freqs)
            if (right-left+1)-max_freq > k:
                freqs[ord(s[left])-ord('A')] -= 1
                left += 1
            res = max(res, right-left+1)
            right += 1

        return res
            

