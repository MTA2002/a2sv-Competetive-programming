class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)

        n = len(heights)
        ans = [0] * n    
        stack = [(-1,-1)] 
        
        for i in range(n):

            while stack and stack[-1][0] > heights[i]:
                val , idx  = stack.pop()
                ans[idx] += (i - idx)

            if stack:
                ans[i] += ((i - stack[-1][1]) - 1) 

            stack.append((heights[i],i))        
        
        for i in range(n):
            ans[i] *= heights[i]

        return max(ans)

