class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = set()
        bucket = [['.'] * n for _ in range(n)]
        visited = Counter()

        def backtrack(r,c):
            if r == n:
                ans.add(tuple(["".join(a) for a in bucket]))
                return

            if visited[(r,c)] <= 0:
                visited[(r,c)] += 1
                
                for i in range(r,n):
                    visited[(i,c)] += 1
                for i in range(r):
                    visited[(i,c)] += 1
                for i in range(c,n):
                    visited[(r,i)] += 1
                for i in range(c):
                    visited[(r,i)] += 1

                sr = r
                sc = c

                while sr < n and sc < n:
                    visited[(sr,sc)] += 1
                    sr += 1
                    sc += 1

                sr = r
                sc = c

                while sr >= 0 and sc < n:
                    visited[(sr,sc)] += 1
                    sr -= 1
                    sc += 1

                sr = r
                sc = c

                while sr < n and sc >= 0:
                    visited[(sr,sc)] += 1
                    sr += 1
                    sc -= 1

                sr = r
                sc = c

                while sr >= 0 and sc >= 0:
                    visited[(sr,sc)] += 1
                    sr -= 1
                    sc -= 1
                bucket[r][c] = 'Q'

                for i in range(n):
                    backtrack(r+1,i)

                bucket[r][c] = '.'
                visited[(r,c)] -= 1
                
                for i in range(r,n):
                    visited[(i,c)] -= 1
                for i in range(r):
                    visited[(i,c)] -= 1
                for i in range(c,n):
                    visited[(r,i)] -= 1
                for i in range(c):
                    visited[(r,i)] -= 1

                sr = r
                sc = c

                while sr < n and sc < n:
                    visited[(sr,sc)] -= 1
                    sr += 1
                    sc += 1

                sr = r
                sc = c

                while sr >= 0 and sc < n:
                    visited[(sr,sc)] -= 1
                    sr -= 1
                    sc += 1

                sr = r
                sc = c

                while sr < n and sc >= 0:
                    visited[(sr,sc)] -= 1
                    sr += 1
                    sc -= 1

                sr = r
                sc = c

                while sr >= 0 and sc >= 0:
                    visited[(sr,sc)] -= 1
                    sr -= 1
                    sc -= 1
                
        for i in range(n):
            backtrack(0,i)
        print(len(ans))

        return ans
