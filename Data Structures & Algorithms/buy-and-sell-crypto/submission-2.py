class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_profit = 0
        max_profit = 0

        for i in range(1, len(prices)):
            daily_change = prices[i] - prices[i-1]
            cur_profit = max(0, cur_profit+daily_change)
            max_profit = max(max_profit, cur_profit)
        return max_profit
