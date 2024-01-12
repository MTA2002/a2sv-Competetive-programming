class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def solve(k):
            counter = 0
            left = 0
            count = 0

            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    counter += 1

                while counter > k:
                    if nums[left] % 2 != 0:
                        counter -= 1

                    left += 1

                count += right - left + 1

            return count
            
        return solve(k) - solve(k-1)
