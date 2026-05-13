class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1
        for key in s_dict:
            if s_dict[key] != t_dict.get(key):
                return False
        return True

#Time: O(n) or more precisely O(s+t), both linear, but O(s+t) shows the presense of two inputs
#Space: O(s+t), creating hashmaps for both strings