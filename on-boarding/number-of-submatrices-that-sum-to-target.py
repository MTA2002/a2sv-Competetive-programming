class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(1,cols):
                matrix[row][col] += matrix[row][col - 1]
        
        count = 0 

        for col1 in range(cols):
            for col2 in range(col1,cols):
                sum_ = 0
                dict_ = Counter()
                dict_[0] = 1
                for row in range(rows):
                    sum_ += matrix[row][col2]
                    sum_ -= matrix[row][col1-1] if col1 - 1 >= 0 else 0
                    if sum_ - target in dict_:
                        count += dict_[sum_ - target]
                    dict_[sum_] += 1
        
        return count

