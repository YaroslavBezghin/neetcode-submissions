class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        l = 0
        r = 1
        while r < len(prices):
            p = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            else:
                m = max(m, p)
            r += 1
        return m