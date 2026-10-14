"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        prevEnd = intervals[0].end
        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            if start < prevEnd:
                return False
            else:
                prevEnd = end
        return True