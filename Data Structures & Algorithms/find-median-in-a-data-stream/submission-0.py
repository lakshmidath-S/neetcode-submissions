import heapq
class MedianFinder:

    def __init__(self):
        self.right=[]
        self.left=[]
    def addNum(self, num: int) -> None:

        if not self.left:
            heapq.heappush(self.left,-num)

        elif -(self.left[0])>=num:
            heapq.heappush(self.left,-num)
            if len(self.left)>len(self.right)+1:
                a=heapq.heappop(self.left)
                heapq.heappush(self.right,-a)
        else:
            heapq.heappush(self.right,num)
            if len(self.left)<len(self.right):
                a=heapq.heappop(self.right)
                heapq.heappush(self.left,-a)

    def findMedian(self) -> float:
        if len(self.left)>len(self.right):
            return  -(self.left[0])
        else:
           return ((-(self.left[0])+self.right[0])/2)
        
        