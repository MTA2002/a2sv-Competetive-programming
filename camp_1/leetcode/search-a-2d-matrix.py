class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        rows , cols = len(matrix) , len(matrix[0])
        low , high = 0 , (rows * cols) - 1

        while low <= high:
            mid = (low + high) // 2
            pos = [mid // cols,mid % cols]
            if matrix[pos[0]][pos[1]] > target:
                high = mid - 1
            elif matrix[pos[0]][pos[1]] < target:
                low = mid + 1
            else:
                return True