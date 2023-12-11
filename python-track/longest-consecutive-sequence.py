class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_count=0
        count=1
        size=len(nums)
        if size==0:
            return 0

        for i in range(size-1):
            if nums[i+1]-nums[i]==1:
                count+=1
            elif nums[i+1]-nums[i]>1:
                max_count=max(max_count,count)
                count=1
        max_count=max(max_count,count)
        
        return max_count