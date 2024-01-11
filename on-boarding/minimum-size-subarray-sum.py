class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_ = float('inf')
        running_sum = 0
        left = 0

        for right in range(len(nums)):
            running_sum += nums[right]

            while running_sum >= target:
                min_ = min(min_,right-left+1)
                running_sum -= nums[left]
                left += 1
        
        return min_ if min_ != float('inf') else 0