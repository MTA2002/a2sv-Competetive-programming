class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        size = len(height)
        left_max = [0] * size
        left_max[0] = height[0] 
        right_max = [0] * size
        right_max[-1] = height[-1]
    

        for i in range(1,size):
            left_max[i] = max(height[i],left_max[i-1])
            right_max[size - i - 1] = max(height[size - i - 1 ],right_max[size - i])
            
        for i in range(1,size-1):
            ans += min(left_max[i],right_max[i]) - height[i]

        return ans