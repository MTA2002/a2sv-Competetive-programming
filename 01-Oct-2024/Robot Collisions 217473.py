# Problem: Robot Collisions - https://leetcode.com/problems/robot-collisions/

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        combined = [(positions[i], healths[i], directions[i], i) for i in range(n)]
        combined.sort()
        stack = []

        for p, h, d, i in combined:
            while stack and stack[-1][1] + d == 'RL':
                if stack[-1][0] > h:
                    stack[-1][0] -= 1
                    h = 0
                    break
                if stack[-1][0] == h:
                    h = 0
                    stack.pop()
                    break
                stack.pop()
                h -= 1
            
            if h > 0:
                stack.append([h, d, i])

        stack.sort(key = lambda x:x[2])
        
        return [stack[i][0] for i in range(len(stack))]