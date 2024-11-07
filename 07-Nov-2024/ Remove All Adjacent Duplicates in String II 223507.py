# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [('.', 1)]

        for ch in s:
            prev, cnt = stack[-1]
            if ch == prev:
                stack.append((ch, cnt + 1))
            else:
                stack.append((ch, 1))
            
            if stack[-1][1] == k:
                count = 0
                cnt = stack[-1][1]
                
                while count < cnt:
                    stack.pop()
                    count += 1
        

        ans = []

        for ch, cnt in stack:
            ans.append(ch)

        return ''.join(ans[1:]) 