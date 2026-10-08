class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # if we can find subset of sum == total/2
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [False] * (target+1)
        dp[0] = True

        for num in nums:
            for s in range(target, num-1, -1):
                if dp[target]:
                    return True
                dp[s] = dp[s] or dp[s-num]
            
        return dp[target]