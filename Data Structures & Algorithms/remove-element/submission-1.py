class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        count = 0
        l = len(nums)
        while val in nums:
            count += 1
            nums.remove(val)
        return l - count
        """
        count = 0
        l = len(nums)
        i = 0
        while i < len(nums):
            if nums[i] == val:
                count += 1
                nums.pop(i)
            else:
                i += 1
        return l - count