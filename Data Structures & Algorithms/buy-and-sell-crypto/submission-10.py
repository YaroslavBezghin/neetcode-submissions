class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, result = 0, 1, 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r
            else:
                result = max(profit, result)
            r += 1
        return result