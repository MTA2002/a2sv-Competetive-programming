class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        one_count = 0
        two_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            elif num == 1:
                one_count += 1
            else:
                two_count += 1
        for i in range(zero_count):
            nums[i] = 0
        for i in range(zero_count,zero_count+one_count):
            nums[i] = 1
        for i in range(zero_count+one_count,len(nums)):
            nums[i] = 2



        