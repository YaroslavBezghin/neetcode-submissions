class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

# Time: O(n), one loop of length up to n, using "in" hashset function is only O(1)
# Space: O(n), creating a hashset of size up to n