class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float('-inf')
        sum_ = 0
        
        for i in range(len(nums)):
            sum_ += nums[i]

            if i + 1 >= k:
                max_sum = max(sum_,max_sum)
                sum_ -= nums[i-(k-1)]

        return max_sum / k