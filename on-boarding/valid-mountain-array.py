class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_idx=0
        max_num=float('-inf')
        size=len(arr)

        for i in range(size):
            if arr[i] > max_num:
                max_num = arr[i]
                max_idx = i
        if max_idx==0 or max_idx==size-1:
            return False

        for i in range(max_idx):
            if arr[i] >= arr [i+1]:
                return False

        for i in range(max_idx,size-1):
            if arr[i] <= arr [i+1]:
                return False
        
        return True
