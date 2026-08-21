class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        one solution is guaranteed, list is sorted and in ascending order,
        meaning we can check if sum of first and last element is bigger or 
        smaller and shift.
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            cur_sum = nums[l] + nums[r]
            if cur_sum < target:
                l += 1
            elif cur_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]