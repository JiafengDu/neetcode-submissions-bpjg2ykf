class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # initialize assume we are currently at n-2,
        two_step = 1 # ways to reach n from two steps up (which is n)
        one_step = 1 # ways to reach n fron one step up (which is n-1)

        for i in range(n-2, -1, -1):
            curr = one_step + two_step
            two_step = one_step
            one_step = curr
        
        return one_step