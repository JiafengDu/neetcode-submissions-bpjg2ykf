class Solution:

    def encode(self, strs: List[str]) -> str:
        strings = [str(len(s))+'#'+s for s in strs]
        return "".join(strings)
    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        result = []
        while i < n:
            length = ""
            while s[i] != '#':
                length += s[i]
                i += 1
            length = int(length)
            i += length+1
            result.append(s[i-length:i])
        return result
            
