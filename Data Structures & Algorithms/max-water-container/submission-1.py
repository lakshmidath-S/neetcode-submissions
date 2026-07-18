class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxAr=0
        while i<j:
            maxAr=max(min(heights[i],heights[j])*(j-i),maxAr)
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
        return maxAr