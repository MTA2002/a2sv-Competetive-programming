class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_ = float('inf')
        stack = []

        for i in range(len(nums)):
            min_ = min(min_,nums[i])

            while stack and nums[stack[-1][0]] <= nums[i]:
                poped = stack.pop()
            
            stack.append((i,min_))

            if len(stack) > 1:
                if nums[stack[-1][0]] > stack[-1][1] and nums[stack[-1][0]] > stack[-2][1]:
                    print(nums[stack[-1][0]],min_)
                    return True

        return False