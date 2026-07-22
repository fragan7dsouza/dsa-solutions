class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        c= { ")":"(","]":"[","}":"{" }

        for char in s:
            if char in c:
                if stack and stack[-1] == c[char]:
                     stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False

