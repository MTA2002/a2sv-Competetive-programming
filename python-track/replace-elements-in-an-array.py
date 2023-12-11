class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_dict={}

        for index,num in enumerate(nums):
            nums_dict[num]=index
        
        for operation in operations:
            key=operation[1]
            value_replaced=operation[0]
            nums_dict[key]=nums_dict.pop(value_replaced)

        for key in nums_dict:
            index=nums_dict[key]
            nums[index]=key
            
        return nums