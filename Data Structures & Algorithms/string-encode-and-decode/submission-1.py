class Solution:

    def encode(self, strs: List[str]) -> str:
        strings = [str(len(s))+'#'+s for s in strs]
        return "".join(strings)
    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        result = []
        while i < n:
            j = s.find('#', i)
            length = int(s[i:j])
            i = j+1+length
            result.append(s[j+1:i])
        return result
            
