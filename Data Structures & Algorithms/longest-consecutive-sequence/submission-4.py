class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max = 0
        for n in seen:
            if n - 1 in seen:
                continue
            else:
                count = 1
                while n + count in seen:
                    count += 1
                if count > max:
                    max = count
        return max

# Time: O(n), has nested loops, however due to few sequences inner loop runs rarely
# Space: O(n), one set of size n