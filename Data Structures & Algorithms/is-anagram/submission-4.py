class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = [0 for _ in range(26)]

        for c in s:
            chars[ord(c)-ord('a')] += 1
        
        for c in t:
            chars[ord(c)-ord('a')] -= 1
        
        for x in chars:
            if x!=0:
                return False
        
        return True