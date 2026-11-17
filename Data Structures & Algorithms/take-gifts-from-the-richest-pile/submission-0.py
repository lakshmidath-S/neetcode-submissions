import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        def sqrt(num):
            i=0
            while not ((i*i)<=num and ((i+1)*(i+1))>num):
                i+=1
            return i
        heap=[]
        for i in gifts:
            heapq.heappush(heap,-i)
        for i in range(k):
            a=heapq.heappop(heap)
            a=sqrt(-a)
            heapq.heappush(heap,-a)
        print(heap)
        return sum(-x for x in heap)