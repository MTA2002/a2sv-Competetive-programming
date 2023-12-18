class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        size=len(s)
        result=[]

        for idx in range(0,size,2*k):
            if size-idx < k:
                if idx==0:
                    reversed_part=s[idx+k-1::-1]
                else:
                    reversed_part=s[idx+k-1:idx-1:-1]
                result.append(reversed_part)
            else:
                if idx==0:
                    reversed_part=s[idx+k-1::-1]
                else:
                    reversed_part=s[idx+k-1:idx-1:-1]
                normal_part=s[idx+k:idx+k+k]
                result.append(reversed_part)
                result.append(normal_part)

        return ''.join(result)
