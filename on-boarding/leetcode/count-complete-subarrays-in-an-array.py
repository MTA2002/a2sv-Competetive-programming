class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        size = len(nums)

        def solve(k):
            counter = Counter()
            left = 0
            count = 0

            for right in range(size):
                counter[nums[right]] += 1

                while len(counter) == k:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        del counter[nums[left]]
                    left += 1
                
                count += right - left + 1
                print(right,left)
            return count

        return int((size * (size + 1)) / 2 - solve(len(Counter(nums))))
