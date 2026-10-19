class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            digits = 0
            while i>0:
                digits+=i&1
                i>>=1
            res.append(digits)
        return res