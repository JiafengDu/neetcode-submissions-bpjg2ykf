class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+","
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        lengthStr = ""
        while i < len(s):
            j = i
            while lengthStr=="" and s[j]!=",":
                j += 1
            length = int(s[i:j])
            i = j+length+1
            res.append(s[j+1:i])
        return res

