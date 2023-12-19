class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        max_sum=float('-inf')
        size=len(nums)
        zero_count=0
        one_count=0
        zeros_sum=[]
        ones_sum=[]

        for idx in range(size):
            if nums[idx]==0:
                zero_count+=1
            if nums[idx]==1:
                one_count+=1
                
            zeros_sum.append(zero_count)
            ones_sum.append(one_count)

        index_dict=Counter()

        for idx in range(size+1):
            current_sum=0

            if idx-1>=0:
                current_sum += zeros_sum[idx-1]

            if idx-1>=0 and idx < size:
                current_sum -= ones_sum[idx-1]
                
            if idx < size:
                current_sum += ones_sum[size-1]

            max_sum=max(max_sum,current_sum)
            index_dict[idx]=current_sum

        result=[]
        
        for key in index_dict:
            if index_dict[key]==max_sum:
                result.append(key)

        return result
