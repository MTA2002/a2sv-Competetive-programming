class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                score = 0

                while stack[-1] != '(':
                    score += stack.pop()

                stack.pop()
                stack.append(max(2 * score , 1))
        
        return sum(stack)