class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=-n
        prod=1.00
        while n:
            if n%2==1:
                prod*=x
            n//=2
            x*=x
        return prod