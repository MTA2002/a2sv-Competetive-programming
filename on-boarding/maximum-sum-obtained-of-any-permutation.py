class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        size = len(nums)
        prefix_sum = [0] * size

        for start,end in requests:
            prefix_sum[start] += 1

            if end + 1 < size:
                prefix_sum[end + 1] -= 1
        
        for i in range(1, size):
            prefix_sum[i] += prefix_sum[i - 1]
        
        prefix_sum.sort(reverse=True)
        nums.sort(reverse=True)

        ans = 0 

        for i in range(size):
            ans += prefix_sum[i] * nums[i]

        return ans % (pow(10,9) + 7)