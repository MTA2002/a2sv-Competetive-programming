class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        west_east = []
        north_south = []

        for i in range(n):
            west_east.append(max(grid[i]))
            max_ = -1
            for j in range(n):
                max_ = max(max_,grid[j][i])
            north_south.append(max_)

        ans = 0
        
        for i in range(n):
            for j in range(n):
                min_ = min(west_east[i],north_south[j])
                ans += min_ - grid[i][j]


        return ans