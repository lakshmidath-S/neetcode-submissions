import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        j=0
        for i in nums:
            heapq.heappush(heap,i)
            if len(heap)>k:
                temp=heapq.heappop(heap)
        return heap[0]
