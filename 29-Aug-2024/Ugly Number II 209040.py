# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        heappush(heap, 1)
        visited = set()
        count = 0

        while heap:
            cur = heappop(heap)
            count += 1

            if count == n:
                return cur
            
            if cur * 2 not in visited:  
                heappush(heap, cur * 2)
                visited.add(cur * 2)
            
            if cur * 3 not in visited:  
                heappush(heap, cur * 3)
                visited.add(cur * 3)
                
            if cur * 5 not in visited:  
                heappush(heap, cur * 5)
                visited.add(cur * 5)