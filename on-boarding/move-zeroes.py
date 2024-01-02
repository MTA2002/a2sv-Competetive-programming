class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            
        for num in nums:
            if num != 0:
                nums[idx] = num 
                idx += 1

        for i in range(zero_count):
            nums[idx] = 0 
            idx += 1
        

        