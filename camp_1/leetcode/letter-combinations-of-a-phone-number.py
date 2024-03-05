class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        }

        ans = []
        bucket = []

        def backtrack(i):
           
            if i == len(digits):
                if bucket:
                    ans.append("".join(bucket))
                return
            
            for c in digit_map[digits[i]]:
                bucket.append(c)
                backtrack(i+1)
                bucket.pop()
            
        
        backtrack(0)

        return ans