class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        def func(n):
            if n<3:
                for i in range(n):
                    dp[n]=n
                return dp[n]
            else:
                if dp[n]!=0:
                    return dp[n]
                else:
                    dp[n]=func(n-1)+func(n-2)
                    return dp[n]
        return func(n)