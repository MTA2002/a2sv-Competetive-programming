class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        size = len(nums)
        sum_ = 0
        nums.sort()
        closest = float('inf')
        for i in range(size):
            new_target = target - nums[i]

            left = i + 1
            right = size - 1

            while left < right:
                new_sum = nums[left] + nums[right]
                if abs(target-(nums[i]+nums[left]+nums[right])) < closest:
                    sum_ = nums[i]+nums[left]+nums[right]
                    closest = abs(target-(nums[i]+nums[left]+nums[right]))
                if new_sum < new_target:
                    left += 1
                elif new_sum > new_target:
                    right -= 1
                else:
                    break



        
        return sum_


