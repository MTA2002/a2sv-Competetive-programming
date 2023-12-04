class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            if 2*i+1>=len(nums):
                break
            value=nums[2*i+1]
            freq=nums[2*i]
            for j in range(freq):
                res.append(value)
        return res