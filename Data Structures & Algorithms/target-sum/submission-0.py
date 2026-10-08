class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        if abs(target) > total_sum or (total_sum + target) % 2 != 0:
            return 0
        
        subset_target = (total_sum + target) // 2
        dp = [0] * (subset_target + 1)
        dp[0] = 1

        for num in nums:
            for s in range(subset_target, num-1, -1):
                dp[s] += dp[s-num]
        return dp[subset_target]