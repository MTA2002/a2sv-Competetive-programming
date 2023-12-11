class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result=[]
        even_index={i for i in range(len(nums)) if nums[i]%2==0}
        even_sum=0
        for index in even_index:
            even_sum+=nums[index]
        
        for val,index in queries:
            original=nums[index]
            nums[index]+=val
            if nums[index]%2==0:
                if index in even_index:
                    even_sum+=val
                else:
                    even_sum+=nums[index]
                    even_index.add(index)
            else:
                if index in even_index:
                    even_sum-=original
                    even_index.remove(index)
            result.append(even_sum)

        return result
