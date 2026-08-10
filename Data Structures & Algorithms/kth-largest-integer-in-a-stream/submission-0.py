class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.count=len(nums)
        self.a=nums
        self.k=k
    def add(self, val: int) -> int:
        self.a.append(val)
        self.a.sort()
        self.count+=1
        return self.a[self.count-self.k]
        
