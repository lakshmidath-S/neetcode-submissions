class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        n=len(heights)
        maxarea=0
        for i in range(n+1):
            if i==n:
                curheight=0
            else:
                curheight=heights[i]
            while stack and heights[stack[-1]]>curheight:
                h=heights[stack.pop()]
                if stack:
                    left=stack[-1]
                else:
                    left=-1
                maxarea=max(maxarea,h*(i-left-1))
            stack.append(i)
        return maxarea