class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones=0
        i=0
        j=0
        while j<len(nums):
            if nums[j]!=1:
                i=j+1
            max_ones=max(max_ones,j-i+1)
            j+=1
        return max_ones