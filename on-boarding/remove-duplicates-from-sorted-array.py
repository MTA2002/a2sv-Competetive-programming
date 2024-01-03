class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0

        for num in nums:
            if num != nums[pointer]:
                pointer += 1
                nums[pointer] = num

        return pointer + 1