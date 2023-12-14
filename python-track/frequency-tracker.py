class FrequencyTracker:

    def __init__(self):
        self.frequency_tracker=defaultdict(int)
        self.frequency_tracker2=defaultdict(int)

    def add(self, number: int) -> None:
        if number in self.frequency_tracker:
            
            self.frequency_tracker2[self.frequency_tracker[number]]-=1
            if self.frequency_tracker2[self.frequency_tracker[number]]==0:
                self.frequency_tracker2.pop(self.frequency_tracker[number])
        self.frequency_tracker[number]+=1
        self.frequency_tracker2[self.frequency_tracker[number]]+=1
        
    def deleteOne(self, number: int) -> None:
        if number in self.frequency_tracker:
            self.frequency_tracker2[self.frequency_tracker[number]]-=1
            if self.frequency_tracker2[self.frequency_tracker[number]]==0:
                self.frequency_tracker2.pop(self.frequency_tracker[number])

            self.frequency_tracker[number]-=1
            if self.frequency_tracker[number]==0:
                self.frequency_tracker.pop(number)
            else:
                self.frequency_tracker2[self.frequency_tracker[number]]+=1
            
            
            
    def hasFrequency(self, frequency: int) -> bool:
        
        #print(self.frequency_tracker2)
        if frequency in self.frequency_tracker2:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)