class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=0
        if n==0:
            return dp[0]
        dp[1]=1
        if n==1:
            return dp[1]
        dp[2]=1
        if n==2:
            return dp[2]
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        return dp[i]