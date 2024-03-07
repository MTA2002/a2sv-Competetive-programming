class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def helper(divisor):
            sum_ = 0

            for num in nums:
                sum_ += ceil(num / divisor)
            
            return sum_

        low , high = 1 ,  max(nums)
        ans = 0

        while low <= high:
            mid = (high + low) // 2

            if helper(mid) <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans