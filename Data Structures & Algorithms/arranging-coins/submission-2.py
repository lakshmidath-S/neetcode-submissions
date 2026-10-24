class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=0
        j=n
        while i<=j:
            middle=(i+j)//2
            coins=(middle*(middle+1))//2
            if coins==n:
                return middle
            elif coins<n:
                i=middle+1
            else:
                j=middle-1
        return j