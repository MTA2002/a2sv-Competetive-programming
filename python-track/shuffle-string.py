class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr=[""] * len(s)
        for i,c in enumerate(s):
            arr[indices[i]]=c
        return ''.join(arr)
        
