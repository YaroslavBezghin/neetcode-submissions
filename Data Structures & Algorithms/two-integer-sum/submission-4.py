class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i in range(len(nums)):
            if nums[i] not in vals:
                vals[nums[i]] = i
            if target - nums[i] in vals:
                i1 = vals[target - nums[i]]
                i2 = i
        return [i1,i2]