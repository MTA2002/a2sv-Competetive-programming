class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        low , high = 0 , n
        ans = 0

        while low <= high:

            mid = (high + low) // 2
            pos = bisect_left(citations,mid)
            print(mid,pos)

            if pos < n and  citations[pos] >= mid:
                if n - pos >= citations[pos]:
                    ans = citations[pos]
                    low = mid + 1
                elif n - pos >= mid:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                high = mid - 1

        
        return ans