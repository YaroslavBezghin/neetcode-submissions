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
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)