class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def comparator(item):
            return math.sqrt(item[0]*item[0] + item[1]*item[1])

        points.sort(key=comparator)

        return points[:k]