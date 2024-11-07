# Problem: Maximum Number of Points with Cost - https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution:
    def maxPoints(self, dp: List[List[int]]) -> int:
        n, m = len(dp), len(dp[0])
        i = 0

        max_ = -inf
        count = 0
        for j in range(m):
            if max_ - count < dp[i][j]:
                max_ = dp[i][j]
                count = 1
            elif max_ + count == dp[i][j]:
                count = 0
            else:
                dp[i][j] = max_ - count
                count += 1

        max_ = -inf
        count = 0
        for j in range(m - 1, -1, -1):
            if max_ - count < dp[i][j]:
                max_ = dp[i][j]
                count = 1
            elif max_ + count == dp[i][j]:
                count = 0
            else:
                dp[i][j] = max_ - count
                count += 1
        
        for i in range(1, n):
            for j in range(m):
                dp[i][j] += dp[i - 1][j]

            max_ = -inf
            count = 0
            for j in range(m):
                if max_ - count < dp[i][j]:
                    max_ = dp[i][j]
                    count = 1
                elif max_ + count == dp[i][j]:
                    count = 0
                else:
                    dp[i][j] = max_ - count
                    count += 1

            max_ = -inf
            count = 0
            for j in range(m - 1, -1, -1):
                if max_ - count < dp[i][j]:
                    max_ = dp[i][j]
                    count = 1
                elif max_ + count == dp[i][j]:
                    count = 0
                else:
                    dp[i][j] = max_ - count
                    count += 1

        return max(dp[-1])