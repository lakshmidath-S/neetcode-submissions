class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        a=sorted(heights)
        for i in range(len(heights)):
            if heights[i]!=a[i]:
                count+=1
        return count