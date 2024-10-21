# Problem: Minimum Obstacle Removal to Reach Corner - https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def inbound(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS
        
        dists = [[inf] * COLS for _ in range(ROWS)]
        dists[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            cur_dist, row, col = heapq.heappop(heap)

            if cur_dist > dists[row][col]:
                continue
            

            for dr, dc in directions:
                cur_row = dr + row
                cur_col = dc + col

                if inbound(cur_row, cur_col):
                    distance = cur_dist + grid[cur_row][cur_col]

                    if distance < dists[cur_row][cur_col]:
                        dists[cur_row][cur_col] = distance
                        heapq.heappush(heap, (distance, cur_row, cur_col))
        
        return dists[-1][-1]