# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = [inf] * n
        prev[src] = 0

        for i in range(k + 1):
            cur = prev[:]

            for u, v, price in flights:
                cur[v] = min(cur[v], prev[u] + price)
            
            prev = cur[:]
        

        return prev[dst] if prev[dst] != inf else -1