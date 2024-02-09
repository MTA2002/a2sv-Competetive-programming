class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        prefix_sum = [0] * size
        prefix_sum[0] = nums[0]

        for i in range(1,size):
            prefix_sum[i] = nums[i] + prefix_sum[i-1]

        min_sum = 0
        max_sum = float('-inf')


        for sum_ in prefix_sum:
            max_sum = max(sum_ - min_sum ,max_sum)  
            min_sum = min(sum_,min_sum)    
  

        return max_sum