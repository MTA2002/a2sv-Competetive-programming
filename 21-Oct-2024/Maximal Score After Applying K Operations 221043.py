# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heappush(heap, -num)
        
        score = 0

        while k:
            cur = -heappop(heap)
            score += cur
            heappush(heap, -ceil(cur / 3))
            k -= 1
        
        return score