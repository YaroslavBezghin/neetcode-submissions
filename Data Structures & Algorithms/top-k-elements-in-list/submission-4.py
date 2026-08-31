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
        
        i = len(count) - 1
        while i > 0:
            for j in range(len(count[i]) - 1, -1, -1):
                if k > 0:
                    result.append(count[i][j])
                    k -= 1
                else:
                    break
            i -= 1
        return result