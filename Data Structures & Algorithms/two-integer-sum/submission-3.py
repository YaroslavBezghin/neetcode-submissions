class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i in range(len(nums)):
            if nums[i] not in vals:
                vals[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in vals:
                i1 = i
                i2 = vals[target - nums[i]]
        return [i2,i1]