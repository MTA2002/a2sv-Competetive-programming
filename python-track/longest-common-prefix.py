class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        isCommon= True
        size=len(strs)
        ans=""
        j=0
        while isCommon and j<len(strs[0]):
            for i in range(size-1):
                if j<len(strs[i]) and j<len(strs[i+1]):
                    if strs[i][j]!=strs[i+1][j]:
                        isCommon=False
                        break
                else:
                    isCommon=False
                    break
            if isCommon:
                j+=1
        
        return strs[0][:j]
