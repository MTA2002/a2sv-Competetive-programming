class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        minimum_time=0
        for i in range(1,len(points)):
            value1=abs(points[i][0]-points[i-1][0])
            value2=abs(points[i][1]-points[i-1][1])
            minimum_time+=max(value1,value2)
        return minimum_time