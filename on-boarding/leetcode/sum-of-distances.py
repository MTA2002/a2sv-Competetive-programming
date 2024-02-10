class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        size = len(nums)
        sum_ = {}
        ans = [0] * size

        for i in range(size):
            if nums[i] in sum_:
                ans[i] += (i * sum_[nums[i]][1]) - sum_[nums[i]][0]
                sum_[nums[i]][0] += i
                sum_[nums[i]][1] += 1
            else:
                sum_[nums[i]] = [i,1]

        sum_ = {}

        for i in range(size-1,-1,-1):
            if nums[i] in sum_:
                ans[i] += sum_[nums[i]][0] - (i * sum_[nums[i]][1])
                sum_[nums[i]][0] += i
                sum_[nums[i]][1] += 1
            else:
                sum_[nums[i]] = [i,1]
        
        return ans

