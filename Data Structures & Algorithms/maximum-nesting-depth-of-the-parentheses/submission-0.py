class Solution:
    def maxDepth(self, s: str) -> int:
        i=0
        count=0
        maxcount=0
        for i in s:
            if i=='(':
                count+=1
            elif i==')':
                count-=1
            maxcount=max(maxcount,count)
        return maxcount