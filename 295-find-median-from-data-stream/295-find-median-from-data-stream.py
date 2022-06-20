from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.nums = SortedList()
        self.n = 0

    def addNum(self, num: int) -> None:
        SortedList.add(self.nums,num)
        self.n += 1
        # print(self.nums)
        
    def findMedian(self) -> float:
        if self.n == 1:
            return self.nums[0]
        if self.n == 2:
            return (self.nums[0]+self.nums[1])/2 
        if self.n % 2 != 0:
            return self.nums[self.n//2]
        else:
            return (self.nums[self.n//2]+self.nums[self.n//2-1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()