class RecentCounter:

    def __init__(self):
        self.arr = []

    def ping(self, t: int) -> int:
        self.arr.append(t)
        count = 0
        new_arr = []
        
        for el in self.arr:
            if el >= t - 3000:
                new_arr.append(el)

        self.arr = new_arr


        return len(new_arr) 

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)