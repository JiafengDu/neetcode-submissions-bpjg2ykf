class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] is the max profit we can get up to ith pos
        # dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1, rob2 = rob2, temp
        
        return rob2