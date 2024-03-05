class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = set()
        bucket = []
        total = sum(candidates)
        poped = []

        def backtrack(start):
            
            bucket_sum = sum(bucket)
            # print(bucket,bucket_sum)

            if bucket_sum == target:
                ans.add(tuple(sorted(bucket[:])))
                return

            if start == n:
                return 
            
            if bucket_sum > target:
                return 
            
            for i in range(start,n):
                if i > 0 and poped and candidates[i] == candidates[i-1] and candidates[i] == poped[-1]:
                    continue
                bucket.append(candidates[i])
                backtrack(i+1)
                bucket.pop()
                poped.append(candidates[i])
            
        backtrack(0)
        res = []    

        for a in ans:
            res.append(list(a))

        return res
        