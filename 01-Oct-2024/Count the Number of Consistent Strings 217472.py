# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0

        for word in words:
            for ch in word:
                if ch not in allowed:
                    break
            else:
                ans += 1
        
        return ans