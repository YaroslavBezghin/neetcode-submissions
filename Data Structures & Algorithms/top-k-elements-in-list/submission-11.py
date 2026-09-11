class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for n in range(len(nums) + 1)]
        result = []
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        for n in freq:
            count[freq[n]].append(n)
        for i in range(len(count) - 1, -1, -1):
            for j in range(len(count[i]) - 1, -1, -1):
                if k > 0:
                    result.append(count[i][j])
                    k -= 1
        return result