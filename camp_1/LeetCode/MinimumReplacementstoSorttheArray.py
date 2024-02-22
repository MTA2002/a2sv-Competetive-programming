class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        max_ = nums[-1]
        count = 0

        for i in range(len(nums) - 2,-1,-1):
            if nums[i] > max_:
                ans = ceil(nums[i]/max_)
                count += ans - 1
                max_ = nums[i]//ans
                print(max_)
            else:
                max_ = nums[i]
        
        return count