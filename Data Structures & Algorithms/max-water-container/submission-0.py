class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAr=0
        for i in range(len(heights)):
            temp=0
            for j in range(i+1,len(heights)):
                temp=max(min(heights[i],heights[j])*(j-i),temp)
            maxAr=max(temp,maxAr)
        return maxAr