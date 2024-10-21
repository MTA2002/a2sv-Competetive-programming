# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        maxs = [[-inf, -1] for _ in range(n)]
        mins = [[-inf, -1] for _ in range(n)]
        max_ = [-inf, -1]
        min_ = [inf, -1]

        for i in range(n - 1, -1, -1):
            if nums[i] > max_[0]:
                max_[0] = nums[i]
                max_[1] = i
            
            if nums[i] < min_[0]:
                min_[0] = nums[i]
                min_[1] = i

            maxs[i] = max_[:]
            mins[i] = min_[:]

        for i in range(n):
            j = i + indexDifference

            if j < n and abs(maxs[j][0] - nums[i]) >= valueDifference:
                return [i, maxs[j][1]]
            
            if j < n and abs(mins[j][0] - nums[i]) >= valueDifference:
                return [i, mins[j][1]]

        return [-1, -1]
