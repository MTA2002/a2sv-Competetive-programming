class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rowSize = len(matrix)
        columnSize = len(matrix[0])
        for i in range(rowSize):
            for j in range(columnSize):
                if i-1>=0 and j-1>=0:
                    if matrix[i][j]!=matrix[i-1][j-1]:
                        return False
        return True