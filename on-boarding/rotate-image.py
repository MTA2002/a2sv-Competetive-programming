class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rotated_matrix=[]
        size=len(matrix)

        for col in range(size):
            single_row=[]
            for row in range(size-1,-1,-1):
                single_row.append(matrix[row][col])
            rotated_matrix.append(single_row)

        for i in range(size):
            for j in range(size):
                matrix[i][j]=rotated_matrix[i][j]