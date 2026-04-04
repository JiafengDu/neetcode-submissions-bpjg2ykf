class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp len of amount+1, dp[i] means the number of ways to reach target i
        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        
        return dp[amount]