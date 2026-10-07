class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = the minimum number of coins we need to make up target i.
        # dp[0] = 0
        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                prev = i-coin
                if prev >= 0:
                    dp[i] = min(dp[i], 1+dp[prev])
        
        print("final DP table:", dp)
        return dp[amount] if dp[amount]!=float("inf") else -1