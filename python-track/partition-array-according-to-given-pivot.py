class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        size=len(nums)
        result=[]

        for i in range(size):
            if nums[i]<pivot:
                result.append(nums[i])
        for i in range(size):
            if nums[i]==pivot:
                result.append(nums[i])
        for i in range(size):
            if nums[i]>pivot:
                result.append(nums[i])
        return result
        