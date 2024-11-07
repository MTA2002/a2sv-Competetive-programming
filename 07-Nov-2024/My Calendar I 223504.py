# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        
        for start_, end_ in self.bookings:
            if start_ <= start <= end_ - 1:
                return False
            
            if start_ <= end - 1 <= end_ - 1:
                return False
            
            if start <= start_ <= end - 1:
                return False
            
            if start <= end_ - 1 <= end - 1:
                return False
        
        self.bookings.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)