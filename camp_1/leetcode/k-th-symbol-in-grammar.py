class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def solve(n,k):
            if n == 1:
                return False

            range_ = 2 ** n / 4
            
            if k <= range_:
                return solve(n-1,k)
            else:
                return not solve(n-1,k-range_)

        

        return 1 if solve(n,k) else 0