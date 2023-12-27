class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        sorted_nums_dict = {}

        for idx,sorted_num in enumerate(sorted_nums):
            if sorted_num not in sorted_nums_dict:
                sorted_nums_dict[sorted_num] = idx
        
        res = []

        for num in nums:
            res.append(sorted_nums_dict[num])
        
        return res