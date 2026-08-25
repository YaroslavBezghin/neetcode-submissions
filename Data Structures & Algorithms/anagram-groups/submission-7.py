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

# Time: O(n*m), iterating through n strings, each length up to m
# Space: O(n*m), n strings of length up to m are stored 