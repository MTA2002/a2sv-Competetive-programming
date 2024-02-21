class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        stack = deque()
        answer = [0] * size

        for i in range(size):

            while stack and stack[-1][0] < temperatures[i]:
                top = stack.pop()
                answer[top[1]] = i - top[1]
            
            stack.append((temperatures[i],i))
        
        return answer
