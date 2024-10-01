# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_n = mean * (n + m) - sum(rolls)
        ans = [total_n // n] * n
        total_n %= n
        print(ans, total_n)
        for i in range(n):
            if total_n:
                ans[i] += 1
                total_n -= 1
        
        return ans if max(ans) <= 6 and min(ans) >= 1 else []