class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opcl = dict(('()', '[]', '{}'))


        for i in range(len(s)):
            
            if s[i] in '([{':
                stack.append(s[i])
            elif len(stack) == 0 or s[i] != opcl[stack.pop()]:
                return False
            
        return len(stack) == 0
