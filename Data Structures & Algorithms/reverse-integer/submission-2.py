class Solution:
    def reverse(self, x: int) -> int:
        Max=2**31-1
        if x<0:
            a=0
            x=x*-1
            while x!=0:
                last_bit=x%10
                x=x//10
                a=(a*10)+last_bit
            return (a*-1) if a<= Max else 0
        elif x==0:
            return 0
        else:
            a=0
            while x:
                last_bit=x%10
                x=x//10
                a=(a*10)+last_bit
            return a if a< Max else 0