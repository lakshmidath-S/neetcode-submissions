class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count=0
        end=float("-inf")
        for i,j in intervals:
            if i>=end:
                count+=1
                end=j
        return len(intervals)-count
        