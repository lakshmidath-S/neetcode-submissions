class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp={}
        def coin(amt,i):
            if (amt,i) in dp:
                return dp[(amt,i)]
            if amt==0:
                dp[(amt,i)]=1
                return 1
            if amt<0:
                dp[(amt,i)]=0
                return 0
            count=0
            for j in range(i,len(coins)):
                count+=coin(amt-coins[j],j)
            dp[(amt,i)]=count
            return count
        return coin(amount,0)