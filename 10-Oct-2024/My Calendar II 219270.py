# Problem: My Calendar II - https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlapped_bookings = []

    def book(self, start: int, end: int) -> bool:

        for idx, booking in enumerate(self.overlapped_bookings):
            s, e = booking

            if start < e and s < end:
                return False
        

        for idx, booking in enumerate(self.bookings):
            s, e = booking

            if start < e and s < end:
                intrsection_s, intrsection_e = max(s, start), min(e, end)
                self.overlapped_bookings.append((intrsection_s, intrsection_e))            
        
        self.bookings.append((start, end))
        
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)