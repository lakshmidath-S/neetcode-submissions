"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start=intervals[:]
        end=intervals[:]
        start.sort(key=lambda x:x.start)
        end.sort(key=lambda x:x.end)
        s,e,n=0,0,len(intervals)
        maxroom=0
        rooms=0
        while s<n and e<n:
            if start[s].start<end[e].end:
                rooms+=1
                s+=1
            else:
                rooms-=1
                e+=1
            maxroom=max(maxroom,rooms)
        return maxroom


