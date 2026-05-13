class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        word = []
        for i in range(1,len(strs[0])+1):
            word.append(strs[0][0:i])
        lon_pref = ""
        for c in word:
            for s in strs:
                if c not in s or s.index(c) != 0:
                    return lon_pref
            lon_pref = c
        return lon_pref 
        """
        prefix = ""
        for i in range(len(strs[0])): # going through every character in first string
            for s in strs:
                if len(s) == i or s[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix