class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        seen = []
        ans = []
        bucket = []

        def backtrack():

            if len(bucket) == n:
                ans.append(bucket[:])
                return
            
            for i in range(n):
                if i in seen:
                    continue
                
                seen.append(i)
                bucket.append(nums[i])
                backtrack()
                seen.pop()
                bucket.pop()

        backtrack()

        return ans                