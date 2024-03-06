class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(capacity):
            days = 0
            sum_ = 0

            for weight in weights:

                sum_ += weight
                if sum_ > capacity:
                    days += 1
                    sum_ = weight

            return days + 1

        
        low , high = max(weights) - 1 , sum(weights) + 1

        while low + 1 < high:
            mid = (low + high) // 2

            if helper(mid) <= days:
                high = mid
            else:
                low = mid

        return high