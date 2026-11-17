import math
import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap=[-x for x in gifts]
        heapq.heapify(heap)
        for i in range(k):
            a=-heapq.heappop(heap)
            heapq.heappush(heap,-math.isqrt(a))
        return -sum(heap)