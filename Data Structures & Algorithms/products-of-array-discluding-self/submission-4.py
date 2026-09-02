class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        m = 1
        zeros = 0
        for n in nums:
            if n != 0:
                m *= n
            else:
                zeros += 1
        for i in range(len(nums)):
            if zeros == 1:
                if nums[i] != 0:
                    result[i] = 0
                else:
                    result[i] = m
            elif zeros > 1:
                result[i] = 0
            else:
                result[i] = m // nums[i]
        return result