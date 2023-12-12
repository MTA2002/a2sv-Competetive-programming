class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer=[]
        nums_map={}
        for i in range(len(nums)):
            if target-nums[i] in nums_map:
                second_index=nums_map[target-nums[i]]
                answer.append(i)
                answer.append(second_index)
                break
            nums_map[nums[i]]=i
            
        return answer
