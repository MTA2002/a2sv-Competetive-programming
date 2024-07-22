# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        @cache
        def dp(row, col):
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return inf
            
            if row == 0:
                return matrix[row][col]
            
            val = matrix[row][col]
            min_ = min(val + dp(row - 1, col) ,val + dp(row - 1, col - 1) , val + dp(row - 1 , col + 1))
            
            return min_
        
        ans = inf

        for i in range(COLS):
            ans = min(ans, dp(ROWS - 1, i))
        
        return ans