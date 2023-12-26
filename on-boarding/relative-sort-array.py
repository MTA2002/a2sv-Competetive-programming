class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_dict = {}

        for idx,num in enumerate(arr2):
            arr2_dict[num] = idx
        
        def customComparator(item):
            if item in arr2_dict:
                return arr2_dict[item]
            return item + 1001

        arr1.sort(key = customComparator)

        return arr1