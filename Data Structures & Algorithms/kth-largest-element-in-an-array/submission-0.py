import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for i in nums:
            heapq.heappush(heap,-i)
        i=0
        temp=0
        while i<k:
            temp=heapq.heappop(heap)
            i+=1
        return -temp
