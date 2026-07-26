class Solution:
    def isHappy(self, n: int) -> bool:
        abc=set()
        def isCyclical(i,abc):
            a=i
            sums=0
            while a:
                last_digit=a%10
                a=a//10
                sums+=(last_digit**2)
            if sums==1:
                return True
            elif sums in abc:
                return False
            else :
                abc.add(sums)
                return isCyclical(sums,abc)
        return isCyclical(n,abc)
        