class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1]]

        for row in range(rowIndex+1):
            temp = []
            if row == 0:
                temp.append([1])
            else:
                for col in range(row+1):
                    if col == 0:
                        temp.append(ans[row-1][col])
                    elif col == row:
                        temp.append(ans[row-1][col-1])
                    else:
                        temp.append(ans[row-1][col] + ans[row-1][col-1])
                ans.append(temp)
            
        return ans[-1]