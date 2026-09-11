class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frs, frt = {}, {}
        for c in s:
            if c in frs:
                frs[c] += 1
            else:
                frs[c] = 1
        for c in t:
            if c in frt:
                frt[c] += 1
            else:
                frt[c] = 1
        for key in frs:
            if frs[key] != frt.get(key):
                return False
        return True