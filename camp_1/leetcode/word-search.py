class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        seen = []

        def backtrack(r,c,i):
            if i == len(word):
                return True
            
            if r - 1 >= 0 and board[r-1][c] == word[i] and (r-1,c) not in seen:
                seen.append((r-1,c))
                if backtrack(r-1,c,i+1):
                    return True
                seen.pop()

            if r + 1 < rows and board[r+1][c] == word[i] and (r+1,c) not in seen:
                seen.append((r+1,c))
                if backtrack(r+1,c,i+1):
                    return True
                seen.pop()
            if c - 1 >= 0 and board[r][c-1] == word[i] and (r,c-1) not in seen:
                seen.append((r,c-1))
                if backtrack(r,c-1,i+1):
                    return True
                seen.pop()
            if c + 1 < cols and board[r][c+1] == word[i] and (r,c+1) not in seen:
                seen.append((r,c+1))
                if backtrack(r,c+1,i+1):
                    return True
                seen.pop()
            
            return False
            
                     


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    seen.append((i,j))
                    if backtrack(i,j,1):
                        return True
                    seen.pop()
        

        return False