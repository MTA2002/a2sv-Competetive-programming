# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS

        def bfs(row, col):
            cells = []
            queue = deque()
            queue.append((row, col))

            while queue:
                row, col = queue.popleft()
                cells.append((row, col))

                for dr, dc in directions:
                    new_row = dr + row
                    new_col = dc + col

                    if inbound(new_row, new_col) and grid2[new_row][new_col]:
                        grid2[new_row][new_col] = 0
                        queue.append((new_row, new_col))
            
            return cells
        
        ans = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid2[row][col]:
                    grid2[row][col] = 0
                    cells = bfs(row, col)

                    for r, c in cells:
                        if grid1[r][c] == 0:
                            break
                    else:
                        ans += 1
        
        return ans