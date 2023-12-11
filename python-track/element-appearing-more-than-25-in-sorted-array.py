class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size=len(arr)
        twent_five_percent=size//4

        arr_dict=defaultdict(int)

        for num in arr:
            arr_dict[num]+=1
        
        for key in arr_dict:
            if arr_dict[key]>twent_five_percent:
                return key
        return