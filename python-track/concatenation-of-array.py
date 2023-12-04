class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size=len(nums)
        ans=[]
        for i in range(2*size):
            ans.append(nums[i%size])
        return ans