class Solution:
    def totalMoney(self, n: int) -> int:
        answer=0
        i=1
        while n>7:
            answer += sum(range(i,7+i))
            print(answer)
            i += 1
            n -= 7
        print(i)
        answer += sum(range(i,n+i))
        return answer