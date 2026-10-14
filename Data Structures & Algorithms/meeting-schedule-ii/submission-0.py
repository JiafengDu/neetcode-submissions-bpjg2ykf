"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # try schedule in list of one room until conflict. Once conflict, add new room to list with the end time
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        rooms = [intervals[0].end]
        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            if start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
        return len(rooms)
        
