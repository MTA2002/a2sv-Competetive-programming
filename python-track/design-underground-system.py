class UndergroundSystem:

    def __init__(self):
        self.check_in_dict=defaultdict(list)
        self.start_end_dict=defaultdict(list)


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_dict[id].append(stationName)
        self.check_in_dict[id].append(t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start=self.check_in_dict[id][0]
        t1=self.check_in_dict[id][1]
        self.check_in_dict[id]=[]
        tup=(start,stationName)
        self.start_end_dict[tup].append(t-t1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tup=(startStation,endStation)
        
        all=self.start_end_dict[tup]
        average=sum(all)/len(all)
        return average


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)