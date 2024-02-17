class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(reverse=True)
        print(points)
        count = 0
        min_ = float('inf')

        for point in points:
            if point[1] < min_:
                count += 1
                min_ = point[0]

        return count