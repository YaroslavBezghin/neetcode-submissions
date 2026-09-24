class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        result = 0
        while l < r:
            small = min(heights[l], heights[r])
            area = small * (r - l)
            result = max(result, area)
            if small == heights[l]:
                l += 1
            else:
                r -= 1
        return result