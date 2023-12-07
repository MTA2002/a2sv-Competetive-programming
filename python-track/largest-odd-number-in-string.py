class Solution:
    def largestOddNumber(self, num: str) -> str:
        answer=""
        size=len(num)
        for i in range(size-1,-1,-1):
          if int(num[i])%2!=0:
            answer=num[:i+1]
            break

        return answer