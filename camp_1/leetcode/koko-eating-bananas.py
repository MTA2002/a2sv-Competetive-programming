class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def helper(capacity):
            hours = 0
            
            for pile in piles:
                hours += ceil(pile/capacity)

            return hours

        low , high = 1 , max(piles)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            check = helper(mid)

            if check <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
