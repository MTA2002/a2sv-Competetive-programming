class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        size = len(nums)
        
        for i in range(1,size):
            nums[i] += nums[i-1] 
        
        for i in range(size):
            sum1 = nums[i-1] if i-1>=0 else 0
            sum2 = nums[size-1] - nums[i]

            if sum1 == sum2:
                return i
        
        return -1