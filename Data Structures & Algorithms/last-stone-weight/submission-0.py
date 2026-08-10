import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone=[]
        for i in stones:
            heapq.heappush(stone,-i)
        while len(stone)>1:
            x=-(heapq.heappop(stone))
            y=-(heapq.heappop(stone))
            if x==y:
                continue
            elif x>y:
                heapq.heappush(stone,y-x)
            else:
                heapq.heappush(stone,x-y)
        if len(stone)==1:
            return -stone[0]
        else :
            return 0

