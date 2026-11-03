class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            if prices[l] < prices[r]:
                continue
            else:
                l = r
        return max_profit