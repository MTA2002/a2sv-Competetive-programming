# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums.append(0)
        ans = [1, nums[0]]
        left = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[left]:
                cur = i - left
                if nums[left] > ans[1]:
                    ans[1] = nums[left]
                    ans[0] = cur
                elif nums[left] == ans[1]:
                    ans[0] = max(cur, ans[0])

                left = i
        
        return ans[0]