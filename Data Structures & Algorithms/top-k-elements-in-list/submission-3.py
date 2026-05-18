class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)] # creates an array of empty arrays, same amount is nums
        fr = {}
        for num in nums: # count how many times each elemnt appears, key-element, value-frequency
            if num not in fr:
                fr[num] = 1
            else:
                fr[num] += 1
        for num, f in fr.items(): # allows to iterate through both keys and values
            count[f].append(num) # count[i], returns an element that appears i times
        result = []
        for i in range(len(count) - 1, -1, -1): # iterating from highest to lowest, decrementing by 1 till 0
            for n in count[i]:
                result.append(n)
                if len(result) == k:
                    return result
# Time: O(n), three loops are O(n)
# Space: O(n), everything that is created is O(n)