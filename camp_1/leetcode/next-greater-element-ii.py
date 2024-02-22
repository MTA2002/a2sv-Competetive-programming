class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        strictly_increasing = []
        size = len(nums)
        ans = [-1] * size

        for i in range(size*2):

            while strictly_increasing and strictly_increasing[-1][1] < nums[i%size]:
                popped = strictly_increasing.pop()
                ans[popped[0]] = nums[i%size]

            strictly_increasing.append((i%size,nums[i%size]))
        
        return ans
