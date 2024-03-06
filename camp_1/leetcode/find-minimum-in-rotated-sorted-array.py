class Solution:
    def findMin(self, nums: List[int]) -> int:
        low , high = 0 , len(nums) - 1
        ans = high

        while low <= high:
            mid = (low + high) // 2
            print(mid,nums[mid],low,high)
            if nums[mid] <= nums[ans]:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return nums[ans]