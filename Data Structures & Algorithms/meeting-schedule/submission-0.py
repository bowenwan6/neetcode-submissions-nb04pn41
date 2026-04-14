"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        n_meetings = len(intervals)
        for i in range(n_meetings - 1):
            start_0 = intervals[i].start
            start_1 = intervals[i+1].start
            end_0 = intervals[i].end
            end_1 = intervals[i+1].end
            if start_0 == start_1 or end_0 > start_1:
                return False
        return True