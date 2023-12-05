class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        perimeter=0
        size=len(nums)
        for i in range(size-2):
            if nums[i]+nums[i+1]>nums[i+2]:
                perimeter=max(perimeter,nums[i]+nums[i+1]+nums[i+2])
        return perimeter