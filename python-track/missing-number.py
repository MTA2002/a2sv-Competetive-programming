class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        my_set=set(nums)
        size=len(nums)

        for i in range(0,size+1):
            if i not in my_set:
                return i
        return