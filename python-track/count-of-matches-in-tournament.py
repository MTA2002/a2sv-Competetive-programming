class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches=0
        while n>1:
            matche=n//2
            n-=matche
            matches+=matche
            print(n)
        return matches