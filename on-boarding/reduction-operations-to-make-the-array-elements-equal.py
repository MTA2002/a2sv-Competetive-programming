class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        nums_count = Counter(nums)
        nums = list(nums_count.keys())
        nums.sort()

        nums_index = {}

        for idx,num in enumerate(nums):
            if num not in nums_index:
                nums_index[num] = idx
        
        operations = 0
        print(nums_index)
        print(nums_count)
        for num in nums_count:
            operations += (nums_index[num] - 0) * nums_count[num]

        return operations