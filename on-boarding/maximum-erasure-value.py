class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_ = float('-inf')
        left = 0
        nums_dict = Counter()
        sum_ = 0

        for right in range(len(nums)):
            nums_dict[nums[right]] += 1
            sum_ += nums[right]

            while nums_dict[nums[right]] > 1:
                nums_dict[nums[left]] -= 1
                sum_ -= nums[left]
                left += 1

            max_ = max(max_,sum_)

        return max_
