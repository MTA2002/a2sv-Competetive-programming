# Problem: Search in Rotated Sorted Array II - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if nums[mid] == nums[right] == nums[left]:
                right -= 1
                left += 1
            else:
                if nums[mid] <= nums[right]:
                    if nums[mid] <= target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if nums[left] <= target <= nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1

        return False