class Solution:
    def average(self, salary: List[int]) -> float:
        size=len(salary)
        max_element=salary[0]
        min_element=salary[0]
        sum=0
        for i in range(size):
            sum+=salary[i]
            max_element=max(max_element,salary[i])
            min_element=min(min_element,salary[i])
        sum-=max_element
        sum-=min_element
        return sum/(size-2)