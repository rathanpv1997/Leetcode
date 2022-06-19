from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        start_index = SortedList.bisect_right(self.calendar,start)
        end_index = SortedList.bisect_left(self.calendar,end)
        if start_index == end_index and start_index % 2 == 0:
            self.calendar.add(end)
            self.calendar.add(start)
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)