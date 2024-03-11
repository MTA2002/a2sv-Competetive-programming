class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        valid_subgrid = defaultdict(set)
        ROWS , COLS = len(board) , len(board[0])

        def calculateKey(row,col):
            if row <= 2:
                if col <= 2:
                    return 0
                elif col <= 5:
                    return 1
                return 2

            elif row <= 5:
                if col <= 2:
                    return 3
                elif col <= 5:
                    return 4
                return 5

            elif row <= 8:
                if col <= 2:
                    return 6
                elif col <= 5:
                    return 7
                return 8

        def isValidColumn(col,num):
            for row in range(9):
                if board[row][col] == str(num):
                    return False

            return True
        
        def isValidRow(row,num):
            for col in range(9):
                if board[row][col] == str(num):
                    return False

            return True
        
        def isValidBoard(row,col,num):
            key = calculateKey(row,col)
            if num not in valid_subgrid[key]:
                valid_subgrid[key].add(num)
                return True
            
            return False 
            

        def insert(row,col,num):
            key = calculateKey(row,col)
            valid_subgrid[key].add(num)


        def backtrack(idx):
            row = idx // COLS
            col = idx % COLS

            if idx == ROWS * COLS:
                return True

            if board[row][col] == '.': 
                for num in range(1,10):
                    if isValidColumn(col,num) and isValidRow(row,num) and isValidBoard(row,col,num):
                        board[row][col] = str(num)
                        if backtrack(idx + 1):
                            return True
                        valid_subgrid[calculateKey(row,col)].remove(num)
                        board[row][col] = "."
            else:
                return backtrack(idx + 1)
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] != '.':
                    insert(row,col,int(board[row][col]))

        backtrack(0)


