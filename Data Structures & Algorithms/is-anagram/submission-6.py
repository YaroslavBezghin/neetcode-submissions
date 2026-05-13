class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        str1 = list(s)
        str2 = list(t)
        d1 = {}
        d2 = {}
        for c in str1:
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 1
        for c in str2:
            if c in d2:
                d2[c] += 1
            else:
                d2[c] = 1
        for key in d1:
            if not (key in d1 and key in d2) or not (d1[key] == d2[key]):
                return False
        return True