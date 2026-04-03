class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        two_back = 1
        one_back = 2

        for i in range(3, n+1):
            curr = one_back + two_back
            two_back = one_back
            one_back = curr
        
        return one_back