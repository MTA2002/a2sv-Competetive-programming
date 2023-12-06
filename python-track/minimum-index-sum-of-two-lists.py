class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minimum_index=float('inf')
        answer=[]

        for i in range(len(list1)):
            if list1[i] in list2:
                index=i+list2.index(list1[i])
                minimum_index=min(index,minimum_index)
                
        for i in range(len(list1)):
            if list1[i] in list2 and i+list2.index(list1[i])==minimum_index:
                answer.append(list1[i])

        return answer
                
