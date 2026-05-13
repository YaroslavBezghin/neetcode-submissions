class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newS = ""
        for i in s:
            if i.isalnum():
                newS += i

        l = list(newS)

        for i in range(len(l)):
            if l[i] != l[len(l) - 1 - i]:
                return False
        return True