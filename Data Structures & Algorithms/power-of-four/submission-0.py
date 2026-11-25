class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def power(num):
            if num==4 or num==1:
                return True
            return False
        if power(n):
            return True
        while not power(n) and n>0:
            n=n/4

        return power(n)