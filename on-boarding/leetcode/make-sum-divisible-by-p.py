class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        nums_index = {}
        target = sum(nums) % p
        min_ = float('inf')

        if target == 0:
            return 0

        running_sum = 0
        nums_index[0] = -1

        for i in range(len(nums)):
            running_sum += nums[i]
            running_sum %= p

            if (running_sum - target) % p  in nums_index:
                min_ = min(min_ ,i - nums_index[(running_sum - target) % p])
            
            nums_index[running_sum] = i
        
        return min_ if min_ < len(nums) else -1



