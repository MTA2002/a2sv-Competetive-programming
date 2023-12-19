class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        size=len(nums)
        count=0
        
        for left in range(size):
            for right in range(left+1,size):
                if nums[left]==nums[right] and left * right % k == 0:
                    count += 1
            
        return count
            
        