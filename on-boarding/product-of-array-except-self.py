class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix = [1] * (size + 1)
        postfix = [1] * (size + 1)

        for i in range(1,size+1):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(size-1,-1,-1):
            postfix[i] = postfix[i+1] * nums[i]

        ans = []
        
        for i in range(size):
            ans.append(prefix[i] * postfix[i+1])

        return ans
        