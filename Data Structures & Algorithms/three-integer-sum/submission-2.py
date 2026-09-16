class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            # if numbers are same it would result copies of triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # if numbers are same it would result copies of triplets
                    # iterate until l and r such that they are different from used l and r 
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return result

# Time: O(n^2), sort O(log(n)), nested loops O(n^2) other two loops move through, O(log(n)) < O(n^2).
# Space: O(1), returned array does not count