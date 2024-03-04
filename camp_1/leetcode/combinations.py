class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        bucket = []

        def backtrack(start):

            if len(bucket) == k:
                ans.append(bucket[:])
            
            for i in range(start,n+1):
                bucket.append(i)
                backtrack(i+1)
                bucket.pop()
            
        
        backtrack(1)

        return ans