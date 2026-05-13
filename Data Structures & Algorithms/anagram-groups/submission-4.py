class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            fr = [0]*26
            for c in s:
                i = ord(c)-ord('a')
                fr[i] += 1
            key = tuple(fr)
            if key not in result:
                result[key] = [s]
            else:
                result[key].append(s)
        return list(result.values())