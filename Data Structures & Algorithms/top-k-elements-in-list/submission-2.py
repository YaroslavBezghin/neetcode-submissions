class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]
        fr = {}
        for num in nums:
            if num not in fr:
                fr[num] = 1
            else:
                fr[num] += 1
        for key, val in fr.items():
            count[val].append(key)
        result = []
        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                result.append(n)
                if len(result) == k:
                    return result