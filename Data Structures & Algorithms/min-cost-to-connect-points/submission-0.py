class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        visited=set()
        min_cost=[float("inf")]*n
        min_cost[0]=0
        total_cost=0
        while(len(visited)<n):
            m=float("inf")
            idx=0
            for i in range(n):
                if i not in visited and min_cost[i]<m:
                    idx=i
                    m=min_cost[i]
            visited.add(idx)
            total_cost+=m
            for j in range(n):
                if j not in visited :
                    new_distance=abs(points[idx][0]-points[j][0])+abs(points[idx][1]-points[j][1])
                    if new_distance<min_cost[j]:
                        min_cost[j]=new_distance
        return total_cost



                