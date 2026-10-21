class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # is today the cheapest price so far
        # if I sold today, best profit so far?
        cheapest = float("inf")
        maxProfit = 0
        for price in prices:
            cheapest = min(cheapest, price)
            maxProfit = max(maxProfit, price - cheapest)
        return maxProfit