class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        size = len(nums)
        prefix_sum = [0] * (size + 1)

        for i in range(1,size+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

        nums_dict = Counter()
        ans = 0

        for sum_ in prefix_sum:

            if sum_ - goal in nums_dict:
                ans += nums_dict[sum_ - goal]

            nums_dict[sum_] += 1
        
        return ans