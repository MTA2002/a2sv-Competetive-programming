# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [(nums[i], i) for i in range(n)]
        nums.sort()
        ans = 0
        max_ = -inf

        for i in range(n - 1, -1, -1):
            if nums[i][1] > max_:
                max_ = nums[i][1]
            else:
                ans = max(ans, max_ - nums[i][1])
        
        return ans