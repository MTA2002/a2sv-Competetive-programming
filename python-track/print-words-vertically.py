class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr=s.split()
        max_value =float('-inf')
        for a in arr:
            max_value=max(max_value,len(a))
        ans=[]
        for i in range(max_value):
            word=""
            for a in arr:
                if i<len(a):
                    word+=a[i]
                else:
                    word+=" "
            ans.append(word.rstrip())
        return ans