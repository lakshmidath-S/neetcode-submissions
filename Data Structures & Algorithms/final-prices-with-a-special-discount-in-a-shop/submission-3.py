class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        ans=prices.copy()
        for i in range(len(prices)-1,-1,-1):
            while stack and stack[-1]>prices[i]:
                stack.pop()
            if stack:
                ans[i]-=stack[-1]
            stack.append(prices[i])
        return ans


            

        
