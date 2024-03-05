class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = set()
        bucket = [['.'] * n for _ in range(n)]
        row_set = set()
        col_set = set()
        diagonals = set()
        anti_diagonals = set()

        def backtrack(r,c):
            if r == n:
                ans.add(tuple(["".join(a) for a in bucket]))
                return

            if r not in row_set and c not in col_set and (r-c) not in diagonals and (r+c) not in  anti_diagonals:
                row_set.add(r)
                col_set.add(c)
                diagonals.add(r-c)
                anti_diagonals.add(r+c)

                bucket[r][c] = 'Q'

                for i in range(n):
                    backtrack(r+1,i)

                bucket[r][c] = '.'
                row_set.discard(r)
                col_set.discard(c)
                diagonals.discard(r-c)
                anti_diagonals.discard(r+c)

                
        for i in range(n):
            backtrack(0,i)

        return ans
