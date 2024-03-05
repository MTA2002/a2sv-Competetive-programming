class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        ans = []
        bucket = []

        def backtrack(start):
            bucket_sum = sum(bucket)

            if start == n:
                return 
            
            if bucket_sum == target:
                ans.append(bucket[:])
                return
            
            if bucket_sum > target:
                return 
            

            for i in range(start,n):
                bucket.append(candidates[i])
                backtrack(i)
                bucket.pop()
            
        backtrack(0)

        return ans
        