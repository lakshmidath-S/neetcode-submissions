class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h==len(piles):
            return max(piles)
        i,j=1,max(piles)
        while i<=j:
            mid=(i+j)//2
            sum=0
            for k in range(len(piles)):
                sum+=(piles[k]+mid-1)//mid
            if sum<=h:
                j=mid-1
            elif sum>h:
                i=mid+1
        return i
    

