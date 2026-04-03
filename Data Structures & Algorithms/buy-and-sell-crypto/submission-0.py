class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy from l, sell at r
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else: # prices[r] is cheaper than l
                l = r
            r += 1

        return maxProfit

        # [10,2,5,1,6,9,1,7,2]
