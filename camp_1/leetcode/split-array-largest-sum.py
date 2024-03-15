class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def helper(capacity):
            days = 0
            sum_ = 0

            for num in nums:

                sum_ += num
                if sum_ > capacity:
                    days += 1
                    sum_ = num

            return days + 1

        
        low , high = max(nums) , sum(nums)
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if helper(mid) <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans