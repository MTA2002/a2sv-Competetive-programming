class Solution:
    def isPalindrome(self, x: int) -> bool:
        xCopy=x
        y=0
        while xCopy > 0 :
            y=y*10+xCopy%10
            xCopy//=10
        return x==y