class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)

        if size % 2 == 0:
            for i in range(size//2):
                for j in range(size//2):
                    matrix[i][j],matrix[j][size-1-i],matrix[size-1-i][size-1-j],matrix[size-1-j][i]=matrix[size-1-j][i],matrix[i][j],matrix[j][size-1-i],matrix[size-1-i][size-1-j]
        else:
            for i in range(size//2+1):
                for j in range(size//2):
                    matrix[i][j],matrix[j][size-1-i],matrix[size-1-i][size-1-j],matrix[size-1-j][i]=matrix[size-1-j][i],matrix[i][j],matrix[j][size-1-i],matrix[size-1-i][size-1-j]


        

        