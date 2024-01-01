class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        size = len(arr)
        def reverse(arr: List[int] , start: int ,end: int):
            new_arr = arr[start:end+1]
            for i in range(len(new_arr)-1,-1,-1):
                arr[start] = new_arr[i]
                start += 1

        for i in range(size+1,0,-1):
            for idx,num in enumerate(arr):
                if num == i:
                    if idx != 0 and idx != i-1:
                        ans.append(idx+1)
                        ans.append(i)
                        reverse(arr,0,idx)
                        reverse(arr,0,i-1)
                    elif idx==0:
                        ans.append(i)
                        reverse(arr,0,i-1)
        return ans
            



        
