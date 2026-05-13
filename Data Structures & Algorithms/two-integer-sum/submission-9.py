class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subtracted = {} # val : index
        for i in range(len(nums)): # for each number save its difference from target and then look for it
            difference = target - nums[i] # find the number that if added to nums[i] is a target
            if nums[i] in subtracted: # check if nums[i] is equal to subtraction in dictionary
                return [subtracted[nums[i]], i]
            else:
                subtracted[difference] = i #save the number that + nums[i] = target, value is it's index

# Time: O(n), itearating throught array with up to n elements
# Space: O(n), creating dictionary with up to n elements