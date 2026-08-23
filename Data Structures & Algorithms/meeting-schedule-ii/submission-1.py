"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        heap=[]
        intervals.sort(key=lambda x:x.start)
        count=0
        for k in range(len(intervals)):
            i,j=intervals[k].start,intervals[k].end
            if not heap:
                heapq.heappush(heap,j)
                count=max(count,len(heap))
                continue
            elif heap[0]<=i:
                heapq.heappop(heap)
            heapq.heappush(heap,j)
            count=max(count,len(heap))
        return count
