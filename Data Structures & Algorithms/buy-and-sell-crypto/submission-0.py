class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        gand=999
        flag=0
        for i in range(len(prices)):
            if prices[i]<gand:
                gand=prices[i] 
                flag=1
            if prices[i]-gand>profit and flag!=0:
                profit=prices[i]-gand
        return profit
            
