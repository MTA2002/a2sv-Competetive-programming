class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        option1=0
        option2=0
        if start<destination:
            option1=sum(distance[start:destination])
            option2=sum(distance[destination:])+sum(distance[0:start])
        else:
            option1=sum(distance[destination:start])
            option2=sum(distance[start:])+sum(distance[0:destination])
        return min(option1,option2)