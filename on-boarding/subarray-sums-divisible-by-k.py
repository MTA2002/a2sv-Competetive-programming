class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        size = len(nums)
        prefix_sum = [0] * (size)

        prefix_sum[0] = nums[0]
        for i in range(1,size):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        ans = 0
        nums_count = Counter()

        for i in range(size):
            if prefix_sum[i] % k == 0:
                ans += 1

            if prefix_sum[i] % k in nums_count:
                ans += nums_count[prefix_sum[i] % k]
            
            nums_count[prefix_sum[i] % k] += 1
            
        return ans