from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        # self.calendar = SortedList()
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        # start_index = SortedList.bisect_right(self.calendar,start)
        # end_index = SortedList.bisect_left(self.calendar,end)
        # if start_index == end_index and start_index % 2 == 0:
        #     self.calendar.add(end)
        #     self.calendar.add(start)
        #     return True
        # return False
        
        start_index = bisect_right(self.calendar,start)
        end_index = bisect_left(self.calendar,end)
        if start_index == end_index and start_index % 2 == 0:
            insort_left(self.calendar,end)
            insort_right(self.calendar,start)
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)