class Solution:
    def isPalindrome(self, s: str) -> bool:
        y = s.lower()
        x = list(y)

        for i in reversed(range(len(x))):
            if not x[i].isalpha() and not x[i].isdigit():
                x.pop(i)
        
        for i in range(len(x)):
            if i == len(x) // 2:
                break
            if not (x[i] == x[len(x) - i - 1]):
                return False
           
        return True
