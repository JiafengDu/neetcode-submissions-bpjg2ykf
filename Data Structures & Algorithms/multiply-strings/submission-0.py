class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # num1=45, num2=123
        #  45*123 = 5*123+4*123*10
        #  5*123 = 5*3+5*2*10+5*1*100
        if num1=="0" or num2=="0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m+n)

        for i in range(m-1, -1, -1):
            d1 = ord(num1[i])-ord('0')
            for j in range(n-1, -1, -1):
                d2 = ord(num2[j])-ord('0')

                total = d1*d2+res[i+j+1]
                res[i+j+1] = total % 10
                res[i+j] += total // 10
        start = 1 if res[0]==0 else 0
        return "".join(map(str, res[start:]))


