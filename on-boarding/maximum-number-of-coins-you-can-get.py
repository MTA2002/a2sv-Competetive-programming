class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left = 0
        right = len(piles) - 2
        total = 0

        while left < right:
            total += piles[right]
            right -= 2
            left += 1
            
        return total
