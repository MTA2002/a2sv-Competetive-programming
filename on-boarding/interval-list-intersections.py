class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []

        left = 0
        right = 0

        while left < len(firstList) and right < len(secondList):
            point1 = firstList[left]
            point2 = secondList[right]
            a = max(point1[0],point2[0])
            b = min(point1[1],point2[1])

            if point1[0] <= a <= point1[1] and point2[0] <= a <= point2[1] and point1[0] <= b <= point1[1] and point2[0] <= b <= point2[1]:
                ans.append([a,b])
            
            if point1[1] < point2[1]:
                left += 1
            elif point1[1] > point2[1]:
                right += 1
            else:
                left += 1
                right += 1
                
        return ans
            
            