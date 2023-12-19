class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed_matrix=[]
        row_size=len(matrix)
        col_size=len(matrix[0])

        for col in range(col_size):
            row_matrix=[]
            for row in range(row_size):
                row_matrix.append(matrix[row][col])
            transposed_matrix.append(row_matrix)
            
        return transposed_matrix