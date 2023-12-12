class OrderedStream:

    def __init__(self, n: int):
        self.ordered_list=[""]*n
        self.available_indexes=set()
        self.pointer=0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.ordered_list[idKey-1]=value
        self.available_indexes.add(idKey-1)
        
        if idKey-1==self.pointer:
            start=self.pointer
            while self.pointer in self.available_indexes:
                self.pointer+=1
            return self.ordered_list[start:self.pointer]
        return []


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)