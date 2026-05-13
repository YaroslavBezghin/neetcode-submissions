class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in parentheses: # checking if c is closing par
                if stack and stack[-1] == parentheses[c]: # if stack isn't empty and the last
#par is matching opening one then take them out
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        return False    