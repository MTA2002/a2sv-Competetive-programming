class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        
        self.prefix_sum = [[0] * cols for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i - 1 >= 0:
                    self.prefix_sum[i][j] += self.prefix_sum[i-1][j]
                if j - 1 >= 0:
                    self.prefix_sum[i][j] += self.prefix_sum[i][j-1]
                if i - 1 >= 0 and j - 1 >= 0:
                    self.prefix_sum[i][j] -= self.prefix_sum[i-1][j-1]
                self.prefix_sum[i][j] += matrix[i][j]
        


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        ans += self.prefix_sum[row2][col2]
        if col1 - 1 >= 0:
            ans -= self.prefix_sum[row2][col1-1]
        if row1 - 1 >= 0:
            ans -= self.prefix_sum[row1-1][col2]
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            ans += self.prefix_sum[row1-1][col1-1]
        return ans
    


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)