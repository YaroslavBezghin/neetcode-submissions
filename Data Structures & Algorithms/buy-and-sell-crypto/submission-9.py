class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,  r = 0, 1
        result = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            result = max(profit, result)
            if prices[l] > prices[r]:
                l = r
            r += 1
        return result