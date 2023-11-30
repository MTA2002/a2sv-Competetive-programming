class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict={}
        pairs_count=0
        for i in nums:
            dict[i]=dict.setdefault(i,0)+1
        for i in dict:
            pairs_count+=(dict[i]*(dict[i]-1))/2
        return int(pairs_count)