class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        max = 0
        for n in nums:
            seen.add(n)
        for n in nums:
            if n - 1 in seen:
                continue
            else:
                i = 0
                count = 1
                while i < len(nums) - 1:
                    if n + i + 1 in seen:
                        count += 1
                        i += 1
                    else:
                        break
                if count > max:
                    max = count
        return max