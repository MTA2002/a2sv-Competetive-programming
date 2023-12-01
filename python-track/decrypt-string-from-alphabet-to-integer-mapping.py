class Solution:
    def freqAlphabets(self, s: str) -> str:
        i=len(s)-1
        res=''
        while i>=0:
            if s[i]=='#':
                res+=chr(int(s[i-2]+s[i-1])+96)
                i-=2
            else:
                res+=chr(int(s[i])+96)
            i-=1
        return res[::-1]