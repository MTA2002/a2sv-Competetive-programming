class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result_dict=defaultdict(list)
        row_size=len(mat)
        col_size=len(mat[0])

        for row in range(row_size):
            for col in range(col_size):
                result_dict[row+col].append(mat[row][col])
        
        result=[]

        for key in result_dict:
            arr=result_dict[key]
            size=len(arr)

            if key%2==0:
                for i in range(size-1,-1,-1):
                    result.append(arr[i]) 
            else:
                for i in range(size):
                    result.append(arr[i])

        return result   
        