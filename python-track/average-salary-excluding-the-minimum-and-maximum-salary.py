class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        size=len(salary)
        sum=0
        for i in range(1,size-1):
            sum+=salary[i]
        return sum/(size-2)