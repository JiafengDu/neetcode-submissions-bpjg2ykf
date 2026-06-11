class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # parse t to map? key, value
        # start, end intialize to 0
        # intialize empty map,
        # start inc end until new map match t_map, if end in key, add to value
        # keep moving start/end pointer to left until exhaust s
        if not t:
            return ""

        t_map, window_map = {}, {}
        for char in t:
            t_map[char] = t_map.get(char, 0)+1
        
        have, need = 0, len(t_map)
        res, res_len = [-1, -1], float("infinity")
        start = 0

        for end in range(len(s)):
            char = s[end]
            window_map[char] = window_map.get(char, 0) + 1
            if char in t_map and window_map[char] == t_map[char]:
                have += 1
            
            while have == need:
                if (end-start+1) < res_len:
                    res = [start, end]
                    res_len = end - start + 1
                
                left_char = s[start]
                window_map[left_char] -= 1
                if left_char in t_map and window_map[left_char] < t_map[left_char]:
                    have -= 1
                
                start += 1
        
        l, r = res
        return s[l:r+1] if res_len != float("infinity") else ""