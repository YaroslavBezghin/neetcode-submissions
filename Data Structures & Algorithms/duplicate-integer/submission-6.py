class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        in_arr = set()
        for n in nums:
            if n in in_arr:
                return True
            in_arr.add(n)
        return False




































"""
        val = set()
        for x in nums:
            if x in val:
                return True
            val.add(x)
        return False
"""