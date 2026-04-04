class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_i1 = 0 # max profit if looking to buy tomorrow (i+1)
        buy_i2 = 0 # max profit if looking to buy the day after tomorrow (i+2)
        sell_i1 = 0 # max profit if looking to sell tomorrow (i+1)

        for i in range(len(prices)-1, -1, -1):
            curr_buy = max(buy_i1, sell_i1 - prices[i])
            curr_sell = max(sell_i1, buy_i2 + prices[i])

            buy_i2 = buy_i1
            buy_i1 = curr_buy
            sell_i1 = curr_sell

        return buy_i1