# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = s.count('a')
        ans1 = inf
        ans2 = 0

        for i in range(len(s)):
            if s[i] == 'b':
                ans1 = min(ans1, ans2 + a_count)
                ans2 += 1

            else:
                a_count -= 1
        
        ans1 = min(ans1, ans2 + a_count)

        return ans1 if ans1 != inf else 0