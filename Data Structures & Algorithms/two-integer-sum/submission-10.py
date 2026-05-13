class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subtracted = {} # val : index
        for i, num in enumerate(nums): 
        # for each number save its difference from target and then look for it
            difference = target - num # find the number that if added to num is a target
            if num in subtracted: # check if num is equal to subtraction in dictionary
                return [subtracted[num], i]
            else:
                subtracted[difference] = i #save the number that + num = target, value is it's index

# Time: O(n), itearating throught array with up to n elements
# Space: O(n), creating dictionary with up to n elements