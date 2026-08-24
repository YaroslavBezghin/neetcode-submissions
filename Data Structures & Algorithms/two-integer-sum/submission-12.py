class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, n in enumerate(nums):
            if target - n in values:
                return [values[target - n], i]
            else:
                values[n] = i
        return

# Time: O(n), one loop of length up to n
# Space: O(n), one hashmap of size up to n