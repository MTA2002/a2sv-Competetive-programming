class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_ = nums[0]
        cur = nums[0]

        for i in range(1,len(nums)):
            cur += nums[i]
            avg = ceil(cur/(i+1))

            max_ = max(avg,max_)

        return max_