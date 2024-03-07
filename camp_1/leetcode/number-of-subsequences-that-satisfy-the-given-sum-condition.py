class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()

        def findValidIndex(num,i):
            low , high = i , len(nums) - 1
            ans = i - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] >= num and nums[mid] + num <= target:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1

            return ans
        
        total = 0

        for i,num in enumerate(nums):
            idx = findValidIndex(num,i)

            if idx >= i:
                total += 2 ** (idx - i)
        
        return total % (10 ** 9 + 7)

