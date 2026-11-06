class Solution:
    def totalMoney(self, n: int) -> int:
        amount=0
        j=0
        i=0
        while n>0:
            if n>=7:
                n-=7
                amount+=28+(i*7)
                i+=1
            else:
                amount+=(n*(n+1+i*2))//2
                n=0
        return amount




