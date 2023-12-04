class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i=0
        longest=""
        for j in range(len(num)):
            if num[j]!=num[i]:
                i=j
            if j-i+1==3:
                longest=max(num[i:j+1],longest)
        return str(longest)

