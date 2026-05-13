class Solution:
    def convert(self, s: List[str]) -> dict:
        d = {}
        for letter in s:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1
        return d

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        str1 = list(s)
        str2 = list(t)
        d1 = self.convert(str1)
        d2 = self.convert(str2)
        
        for key in d1:
            if not (key in d2) or not (d1[key] == d2[key]):
                return False
        return True