class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        need = len(count_t)
        have = 0
        res, res_len = [-1, -1], float("inf")
        l = 0

        window = {}
        for r in range(len(s)):
            char = s[r]
            window[char] = 1+window.get(char, 0)
            if char in count_t and window[char] == count_t[char]:
                have += 1
        
            while have == need:
                if (r-l+1) < res_len:
                    res = [l, r]
                    res_len = r-l+1

                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1

                l += 1
        
        l, r = res
        return s[l:r+1] if res_len !=float("inf") else ""