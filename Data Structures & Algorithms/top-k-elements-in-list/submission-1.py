class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)] # creates an array of empty arrays, same amount is nums
        fr = {}
        for num in nums:
            if num not in fr:
                fr[num] = 1
            else:
                fr[num] += 1
        for num, f in fr.items(): # allows to iterate through both keys and values
            count[f].append(num)
        result = []
        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                result.append(n)
                if len(result) == k:
                    return result