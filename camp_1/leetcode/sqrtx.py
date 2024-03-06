class Solution:
    def mySqrt(self, x: int) -> int:
        low , high = -1 , x + 1

        while low + 1 < high:

            mid = (low + high) // 2

            if mid * mid <= x:
                low = mid
            else:
                high = mid
        
        return low

