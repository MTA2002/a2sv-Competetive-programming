class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones=[]
        for i in range(len(boxes)):
            if boxes[i]=="1":
                ones.append(i)
        print(ones)
        answer=[]
        for i in range(len(boxes)):
            sum=0
            for one in ones:
                sum+=abs(one-i)
            answer.append(sum)
        return answer