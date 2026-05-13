class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        for i in range(len(nums)):
            x = nums[i]
            for j in range(i + 1, len(nums)):
                if x == nums[j]:
                    return True
        return False
        """

        """
        values = set()
        values.add()
        5 in values -> bool
        values.remove()
        len(values)
        """
        val = set()
        for x in nums:
            if x in val:
                return True
            val.add(x)
        return False
