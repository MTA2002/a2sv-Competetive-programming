class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        wildest=float('-inf')
        size=len(points)

        for idx in range(size-1):
            difference = points[idx+1][0] - points[idx][0]
            wildest = max(wildest,difference)
        
        return wildest

