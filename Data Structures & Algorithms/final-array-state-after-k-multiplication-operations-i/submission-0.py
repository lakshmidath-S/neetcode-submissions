import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap=[(nums[x],x) for x in range(len(nums))]
        heapq.heapify(heap)
        for i in range(k):
            a,b=heapq.heappop(heap)
            heapq.heappush(heap,(a*multiplier,b))
        res=[0]*len(nums)
        for a,b in heap:
            res[b]=a
        return res