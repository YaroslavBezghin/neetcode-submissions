class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for n in seen:
            if n - 1 in seen:
                continue
            count = 1
            while n + count in seen:
                count += 1
            longest = max(count, longest)
        return longest