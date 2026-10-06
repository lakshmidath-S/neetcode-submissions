class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        j=x
        while i<=j:
            middle=(i+j)//2
            if middle*middle<=x and (middle+1)*(middle+1)>x:
                return middle
            elif middle*middle<x:
                i=middle+1
            else:
                j=middle-1
        return i