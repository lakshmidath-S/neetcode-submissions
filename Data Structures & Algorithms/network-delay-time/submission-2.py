import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap=[(0,k)]
        distance=[float('inf')]*(n+1)
        distance[0]=0
        distance[k]=0
        graph=defaultdict(list)
        for i in times:
            source=i[0]
            end=i[1]
            cost=i[2]
            graph[source].append((end,cost))
        while heap:
            d,node=heapq.heappop(heap)
            if d>distance[node]:
                continue
            for i in graph[node]:
                dest=i[0]
                newdistance=d+i[1]
                if distance[dest]>newdistance:
                    distance[dest]=newdistance
                    heapq.heappush(heap,(newdistance,dest))
        max_distance=max(distance[1:])
        return  max_distance if max_distance!=float('inf') else -1


        