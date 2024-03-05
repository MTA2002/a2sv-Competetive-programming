class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0

        while i < len(s):
            
            if s[i] == '(':
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            else:
                if stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                else:
                    return False
                
            i += 1
        
        return len(stack) == 0

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        bucket = []
        parenthesis = '()'

        def backtrack():

            if len(bucket) == n * 2:
                s = "".join(bucket)
                if self.isValid(s):
                    ans.append(s)
                return
            
            for i in range(2):
                bucket.append(parenthesis[i])
                backtrack()
                bucket.pop()
            
        
        backtrack()
        
        return ans