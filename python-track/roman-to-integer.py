class Solution:
    def romanToInt(self, s: str) -> int:
        dict={}
        size=len(s)
        dict['I']=1
        dict['V']=5
        dict['X']=10
        dict['L']=50
        dict['C']=100
        dict['D']=500
        dict['M']=1000
        result=0
        i=0
        while i<size:
            if i+1<size:
                if s[i]=='I':
                    if s[i+1]=='V' or s[i+1]=='X':
                        result+=dict[s[i+1]]
                        result-=dict['I']
                        i+=2
                        continue
                elif s[i]=='X':
                    if s[i+1]=='L' or  s[i+1]=='C':
                        result+=dict[s[i+1]]
                        result-=dict['X']
                        i+=2
                        continue
                elif s[i]=='C':
                    if s[i+1]=='D' or  s[i+1]=='M':
                        result+=dict[s[i+1]]
                        result-=dict['C']
                        i+=2
                        continue
            result+=dict[s[i]]
            i+=1
        return result
