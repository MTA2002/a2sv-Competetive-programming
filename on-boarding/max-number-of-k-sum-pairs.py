class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            sum_ = nums[left] + nums[right]

            if sum_ > k:
                right -= 1
            elif sum_ < k:
                left += 1
            else:
                count += 1
                left += 1
                right -= 1
        
        return count

     