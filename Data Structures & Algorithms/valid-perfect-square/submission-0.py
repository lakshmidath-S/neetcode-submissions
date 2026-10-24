class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=0
        j=num
        while i<=j:
            middle=(i+j)//2
            sqr=middle*middle
            if sqr==num:
                return True
            elif sqr>num:
                j=middle-1
            else:
                i=middle+1
        return False