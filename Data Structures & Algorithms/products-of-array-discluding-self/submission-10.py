class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        prefix = [1]
        for i in range(len(nums) - 1):
            prefix.append(prefix[i] * nums[i])
        postfix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * postfix[i])
        return result
        """
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result