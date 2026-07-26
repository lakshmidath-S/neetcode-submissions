class Solution:
    def isHappy(self, n: int) -> bool:
        abc=set()
        def isCyclical(i,abc):
            a=i
            sum=0
            while a:
                last_digit=a%10
                a=a//10
                sum+=(last_digit**2)
            if sum==1:
                return True
            elif sum in abc:
                return False
            else :
                abc.add(sum)
                return isCyclical(sum,abc)
        return isCyclical(n,abc)
        