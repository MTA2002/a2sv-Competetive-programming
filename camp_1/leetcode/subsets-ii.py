class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        bucket = []
        nums.sort()
        
        def backtrack(start):
            if bucket[:] not in ans:
                ans.append(bucket[:])
            
            for i in range(start,len(nums)):
                bucket.append(nums[i])
                backtrack(i+1)
                bucket.pop()
            
        
        backtrack(0)

        return ans