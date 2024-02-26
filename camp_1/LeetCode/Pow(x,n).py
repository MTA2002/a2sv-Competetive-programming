class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            res = pow(x,n//2)
            res *= res
            if n % 2 == 1:
                res *= x
            return res

        
        isNegative = n < 0

        return 1 / pow(x,abs(n)) if isNegative else pow(x,n)