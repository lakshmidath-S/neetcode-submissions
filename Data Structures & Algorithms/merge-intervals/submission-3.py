class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        j=intervals[0][0]
        k=intervals[0][1]
        i=1
        ans=[]
        while i<len(intervals):
            a=intervals[i][0]
            b=intervals[i][1]
            if a<=k:              #merge
                k=max(k,b)           
            else:  # no merge
                ans.append([j,k]) 
                j=a
                k=b
            i+=1
        ans.append([j,k]) 
        return ans