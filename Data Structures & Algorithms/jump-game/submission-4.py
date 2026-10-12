class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp[i] - boolean of the last index is reachable from index i
        # base - dp[n-1] = True
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True

        for i in range(n-2, -1, -1):
            jump = nums[i]
            dp[i] = any(dp[i+1:min(i+jump+1,n)])
        return dp[0]        
        