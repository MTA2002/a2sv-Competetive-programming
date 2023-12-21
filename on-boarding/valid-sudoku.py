class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size=len(board)

        for row in range(size):
            row_set = set()
            col_set = set()
            for col in range(size):
                if board[row][col] in row_set or board[col][row] in col_set:
                    return False

                if board[row][col].isdigit(): 
                    row_set.add(board[row][col])    
                if board[col][row].isdigit(): 
                    col_set.add(board[col][row])

        for row in range(0,size,3):
            for col in range(0,size,3):
                s=set()
                for row_ins in range(row,row+3):
                    for col_ins in range(col,col+3):
                        if board[row_ins][col_ins].isdigit() == False: 
                            continue

                        if board[row_ins][col_ins] in s:
                            print()
                            return False
                        s.add(board[row_ins][col_ins])
                        
        return True
                
