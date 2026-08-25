class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            frequency = [0] * 26
            for c in s:
                index = ord(c) - ord("a")
                frequency[index] += 1
            key = tuple(frequency)
            if key in result:
                result[key].append(s)
            else:
                result[key] = [s]
        return list(result.values())