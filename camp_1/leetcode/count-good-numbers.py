class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        def pow(x,n):
            if n == 0:
                return 1

            if n == 1:
                return x

            res = pow(x,n//2) % MOD
            res *= res 

            if n % 2 == 1:
                res *= x

            return res % MOD
        
        power = n / 2
        
        first = pow(5,ceil(power))
        second = pow(4,floor(power))
        
        return (first * second ) % MOD