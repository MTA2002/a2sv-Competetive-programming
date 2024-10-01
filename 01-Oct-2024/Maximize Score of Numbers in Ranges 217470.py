# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, starts: List[int], d: int) -> int:
        starts.sort()

        def check(point):
            start = starts[0]

            for i in range(1, len(starts)):
                if start + point > starts[i] + d:
                    return False
                
                start += point

                if start < starts[i]:
                    start = starts[i]
            
            return True

        left, right = 0, 10 ** 15

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right