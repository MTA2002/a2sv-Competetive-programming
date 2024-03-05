class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        bucket = []

        def backtrack(start):
            bucket_sum = sum(bucket)
            if len(bucket) == k:
                if bucket_sum == n:
                    ans.append(bucket[:])
                return
                
            if bucket_sum > n:
                return
            
            for i in range(start,10):
                bucket.append(i)
                backtrack(i+1)
                bucket.pop()
            
        
        backtrack(1)

        return ans