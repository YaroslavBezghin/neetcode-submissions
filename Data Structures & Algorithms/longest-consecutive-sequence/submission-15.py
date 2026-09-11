class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_len = 0
        for n in seen:
            if n - 1 not in seen:
                count = 1
                while n + count in seen:
                    count += 1
                max_len = max(max_len, count)
        return max_len