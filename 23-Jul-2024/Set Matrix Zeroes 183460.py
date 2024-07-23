# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    r = row + 1
                    c = col
                    while r < rows:
                        if  matrix[r][c] == 0:
                           break
                        matrix[r][c] = 2147483648
                        r += 1 
                    r = row - 1
                    c = col
                    while r >= 0:
                        if  matrix[r][c] == 0:
                           break
                        matrix[r][c] = 2147483648
                        r -= 1 
                    r = row
                    c = col + 1
                    while c < cols:
                        if  matrix[r][c] == 0:
                           break
                        matrix[r][c] = 2147483648
                        c += 1 
                    r = row
                    c = col - 1
                    while c >= 0:
                        if  matrix[r][c] == 0:
                           break
                        matrix[r][c] = 2147483648
                        c -= 1 
        print(matrix)
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 2147483648:
                    matrix[row][col] = 0
            
                