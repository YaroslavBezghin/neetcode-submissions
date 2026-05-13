class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1, t1 = {}, {}
        for ch in s:
            if ch in s1:
                s1[ch] += 1
            else:
                s1[ch] = 1
        for ch in t:
            if ch in t1:
                t1[ch] += 1
            else:
                t1[ch] = 1
        for key in s1:
            if key not in t1 or s1[key] != t1[key]:
                return False
        return True