class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        fronts_dict=defaultdict(list)
        backs_dict=defaultdict(int)
        size=len(fronts)
        good=float('inf')

        for index,num in enumerate(fronts):
            fronts_dict[num].append(index)
            
        for index,num in enumerate(backs):
            if num not in fronts_dict:
                good=min(good,num)
            backs_dict[index]=num
        
        for i in range(size):
            flag=True
            for j in fronts_dict[fronts[i]]:
                if backs_dict[j]==fronts[i]:
                     flag=False
                     break
            
            if flag:
                good=min(good,fronts[i]) 
                print(good)

        if good==float('inf'):
            return 0           

        return good