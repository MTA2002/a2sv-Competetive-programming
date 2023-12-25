class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        guarded_cells = set()
        grid = [[0]*n  for _ in range(m)]
        for guard in guards:
            grid[guard[0]][guard[1]] = 'G'
        for wall in walls:
            grid[wall[0]][wall[1]] = 'W'
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 'G':
                    for i in range(col+1,n):
                        if grid[row][i] == 'W' or grid[row][i] == 'G':
                            break
                        guarded_cells.add((row,i))
                    for i in range(col-1,-1,-1):
                        if grid[row][i] == 'W' or grid[row][i] == 'G':
                            break
                        guarded_cells.add((row,i))
                    for i in range(row+1,m):
                        if grid[i][col] == 'W' or grid[i][col] == 'G':
                            break
                        guarded_cells.add((i,col))
                    for i in range(row-1,-1,-1):
                        if grid[i][col] == 'W' or grid[i][col] == 'G':
                            break
                        guarded_cells.add((i,col))
                    
        unguarded_cells = n*m - len(guarded_cells) - len(guards) - len(walls)
        
        return unguarded_cells
