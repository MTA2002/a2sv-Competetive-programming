class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low , high = -1 , len(nums)

        while low + 1 < high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                high = mid
            else:
                low = mid
        
        return high