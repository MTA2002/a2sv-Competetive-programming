# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_, max_ = arrays[0][0], arrays[0][-1]
        ans = -inf

        for i in range(1, len(arrays)):
            ans = max(ans, abs(max_ - arrays[i][0]), abs(arrays[i][-1] - min_))
            min_ = min(min_, arrays[i][0])
            max_ = max(max_, arrays[i][-1])
        
        return ans
