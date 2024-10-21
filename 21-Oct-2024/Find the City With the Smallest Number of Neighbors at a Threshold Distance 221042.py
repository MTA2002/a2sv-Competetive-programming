# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[inf] * n for _ in range(n)]

        for i in range(n):
            graph[i][i] = 0
        
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
        ans = -1
        min_ = inf

        for i in range(n):
            cur = sum(1 for w in graph[i] if w <= distanceThreshold) - 1
            if cur <= min_:
                ans = i
                min_ = cur
        
        return ans