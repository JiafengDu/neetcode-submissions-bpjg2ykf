class MedianFinder:

    def __init__(self):
        # use two heap, one track lower half, one track higher half
        self.lower_half = [] # biggest value on top, so we continuing to pop the top (-num) to the higher half
        self.higher_half = [] # smaller value on top

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower_half, -num)
        heapq.heappush(self.higher_half, -heapq.heappop(self.lower_half))
        if len(self.higher_half) > len(self.lower_half):
            num = heapq.heappop(self.higher_half)
            heapq.heappush(self.lower_half, -num)
        
    def findMedian(self) -> float:
        if len(self.higher_half)==len(self.lower_half):
            return (self.higher_half[0]-self.lower_half[0])/2
        else:
            return -self.lower_half[0]

        
        