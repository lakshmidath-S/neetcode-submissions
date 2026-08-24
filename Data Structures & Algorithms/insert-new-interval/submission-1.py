class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start,end=newInterval
        i=0 
        while i< len(intervals) and intervals[i][1]<start:
            i+=1
        left=i
        while i< len(intervals) and intervals[i][0]<=end:
            start=min(start,intervals[i][0])
            end=max(end,intervals[i][1])
            i+=1
        
        return intervals[:left]+[[start,end]]+intervals[i:]