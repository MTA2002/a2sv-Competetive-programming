class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        while i < len(s):
            
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            else:
                if stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                elif stack[-1] == '{' and s[i] == '}':
                    stack.pop()
                elif stack[-1] == '[' and s[i] == ']':
                    stack.pop()
                else:
                    return False
                
            i += 1
        
        return len(stack) == 0