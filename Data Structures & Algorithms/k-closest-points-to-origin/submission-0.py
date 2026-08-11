import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist={}
        heap=[]
        i=0
        for x,y in points:
            a=math.sqrt((x**2)+(y**2))
            heapq.heappush(heap,[a,[x,y]])
        ans=[]
        for i in range(k):
            s=heapq.heappop(heap)
            ans.append(s[1])
        return ans
