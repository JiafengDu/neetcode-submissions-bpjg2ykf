class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        min_limit = -2**31
        max_limit = 2**31 - 1

        while x != 0:
            digit = int(math.fmod(x, 10))
            x = math.trunc(x/10)

            if res > max_limit // 10 or (res == max_limit and digit>7):
                return 0
            if res < math.trunc(min_limit/10) or (res==math.trunc(min_limit/10) and digit<-8):
                return 0
            
            res = res*10 + digit
        
        return res