class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum=float('-inf')
        row_size=len(grid)
        col_size=len(grid[0])

        for i in range(row_size):
            for j in range(col_size):
                current_sum=0
                if (i-1>=0 and i+1 < row_size) and (j-1>=0 and j+1 < col_size):
                    current_sum += grid[i-1][j-1]
                    current_sum += grid[i-1][j]
                    current_sum += grid[i-1][j+1]
                    current_sum += grid[i][j]
                    current_sum += grid[i+1][j-1]
                    current_sum += grid[i+1][j]
                    current_sum += grid[i+1][j+1]

                    max_sum=max(current_sum,max_sum)

        return max_sum
