class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        bucket = []

        def backtrack(start):
            ans.append(bucket[:])
            
            for i in range(start,len(nums)):
                bucket.append(nums[i])
                backtrack(i+1)
                bucket.pop()
            
        
        backtrack(0)

        return ans