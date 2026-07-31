"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        for i in range(len(intervals)):
            if i==0:
                start=intervals[0].start
                end=intervals[0].end
                continue
            if intervals[i].start<end:
                return False
            else:
                end=max(end,intervals[i].end)
                start=intervals[i].start

        return True

    
