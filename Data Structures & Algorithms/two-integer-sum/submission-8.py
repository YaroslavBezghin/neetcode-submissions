class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subtracted = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if nums[i] in subtracted:
                return [subtracted[nums[i]], i]
            else:
                subtracted[difference] = i