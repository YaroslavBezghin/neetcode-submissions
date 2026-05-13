class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            sorted_str = sorted(s) # anagrams will have same sorted s, so use it as a key
            key = tuple(sorted_str)
            if key not in ans:
                ans[key] = [s] # creating a list of str that are anagrams
            else:
                ans[key].append(s)
        return list(ans.values()) # returns list of values, each value is a group of anagrams