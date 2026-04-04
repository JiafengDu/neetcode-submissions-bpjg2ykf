class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy_dp[i] means the maxProfit of buying on ith day
        # sell_dp[j] means the maxProfit of selling on jth day
        dp = {}

        def dfs(i, buying):
            if i>=len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                rest = dfs(i+1, buying)
                dp[(i, buying)] = max(buy, rest)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                rest = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, rest)
            
            return dp[(i, buying)]


        return dfs(0, True)
