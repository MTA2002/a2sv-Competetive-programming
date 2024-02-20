class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        curr_sum = 0
        count = 0

        for num in nums:
            if num > n:
                break
            while num > curr_sum + 1:
               curr_sum += curr_sum + 1
               count += 1
            curr_sum += num
            
        while curr_sum < n:
            curr_sum += curr_sum + 1
            count += 1

        return count


