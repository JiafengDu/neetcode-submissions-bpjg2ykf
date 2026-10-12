class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # if we think which balloon to pop first, subproblems are dependent on each other. Because the subporoblems are coupled and depend on the exact order of previous bursts, greedy choice properties do not hold
        # instead of choosing which balloon to burst first, we choose which balloon to burst last within a range (l, r)
        # when a balloon is the last to burst in (l, r), its neighbors are fixed and known (nums[l-1] and nums[r+1]), decoupling the subproblem into independent ranges.
        # dp[l][r] = max of the list of k range from l to r: dp[l][k-1]+dp[k+1][r]+padded[l-1]*padded[k]*padded[r+1]
        filtered = [x for x in nums if x>0]
        if not filtered:
            return 0
        
        padded = [1] + filtered + [1]
        n = len(filtered)

        dp = [[0]*(n+2) for _ in  range(n+2)]
        for length in range(1, n+1):
            for l in range(1, n-length+2):
                r = l+length-1
                max_coins = 0
                for k in range(l, r+1):
                    coins = dp[l][k-1] + dp[k+1][r] + padded[l-1]*padded[k]*padded[r+1]
                    max_coins = max(max_coins, coins)
                dp[l][r] = max_coins
        return dp[1][n]