import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i=0
        j=0
        ans=[]
        heap=[]
        while len(heap)<k:
            heapq.heappush(heap,(-nums[j],j))
            j+=1
        while j<=len(nums):
            ans.append(-heap[0][0])
            if j < len(nums):
                heapq.heappush(heap,(-nums[j],j))
            j+=1
            i+=1
            while heap and heap[0][1]<i:
                heapq.heappop(heap)
        return ans
