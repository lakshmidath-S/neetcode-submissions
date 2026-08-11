import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        i=0
        for x,y in points:
            a=-((x**2)+(y**2))
            heapq.heappush(heap,[a,[x,y]])
            if len(heap)>k:
                heapq.heappop(heap)
        return[point for dist,point in heap]