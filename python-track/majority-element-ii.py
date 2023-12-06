class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency_count_dictionary={}
        size_of_nums=len(nums)

        for i in nums:
            frequency_count_dictionary[i]=frequency_count_dictionary.setdefault(i,0)+1
        
        answer=[]

        for i in frequency_count_dictionary:
            if frequency_count_dictionary[i] > (size_of_nums//3):
                answer.append(i)
        
        return answer