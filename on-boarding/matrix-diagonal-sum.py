class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size=len(mat)
        diagonal_sum=0

        for row in range(size):
            for col in range(size):
                if col-row == 0:
                    diagonal_sum += mat[row][col]

                if col+row == size-1:
                    diagonal_sum += mat[row][col]

        if size % 2 != 0:
            diagonal_sum -= mat[size//2][size//2]


        return diagonal_sum