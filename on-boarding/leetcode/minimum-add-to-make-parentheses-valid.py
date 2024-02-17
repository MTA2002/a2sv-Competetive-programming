class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        length = len(s)
        count = 0
        total = 0

        for i in range(length):
            if s[i] == '(':
               count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    total += 1
        
        count = 0

        for i in range(length - 1 , -1 ,-1):
            if s[i] == ')':
               count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    total += 1


        return total