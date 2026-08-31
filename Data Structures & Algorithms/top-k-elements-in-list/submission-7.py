class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for n in nums:
            if n in frequency:
                frequency[n] += 1
            else:
                frequency[n] = 1

        count = [[] for n in range(len(nums) + 1)]
        for key in frequency:
            count[frequency[key]].append(key)

        result = []
        for i in range(len(count) - 1, -1, -1):
            for j in range(len(count[i])):
                if k > 0:
                    result.append(count[i][j])
                    k -= 1
                else:
                    break 
        return result