class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr=[]
        for i in nums:
            if i!=val:
                arr.append(i)
        for i in range(len(arr)):
            nums[i]=arr[i]
        return len(arr)