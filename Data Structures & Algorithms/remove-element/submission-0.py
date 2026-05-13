class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        l = len(nums)
        while val in nums:
            count += 1
            nums.remove(val)
        return l - count
