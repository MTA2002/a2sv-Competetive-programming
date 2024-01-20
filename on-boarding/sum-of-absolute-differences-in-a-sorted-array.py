class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix_sum = [0] * size
        prefix_sum[0] = nums[0]
        for i in range(1,size):
            prefix_sum[i] += prefix_sum[i-1] + nums[i]
        
        res = []

        for i in range(size):
            ans = 0
            ans += i * nums[i]
            ans -= prefix_sum[i-1] if i-1 >= 0 else 0
            ans += prefix_sum[-1] - prefix_sum[i]
            ans -= (size - i - 1) * nums[i]
            res.append(ans)

        return res