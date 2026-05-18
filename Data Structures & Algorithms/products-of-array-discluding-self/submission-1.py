class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = [nums[0]] * len(nums)
        postfix = [nums[len(nums) - 1]] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
        for i in range(len(nums) - 2, 0, -1):
            postfix[i] = postfix[i + 1] * nums[i]
        result.append(postfix[1])
        for i in range(1, len(nums) - 1):
            result.append(prefix[i - 1] * postfix[i + 1])
        result.append(prefix[len(nums) - 2])
        return result