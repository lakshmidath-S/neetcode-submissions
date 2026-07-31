class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*n for _ in range(m)]
        def dyna(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            if i==m-1 or j==n-1:
                dp[i][j]=1
                return 1
            dp[i][j]=dyna(i+1,j)+dyna(i,j+1)
            return dp[i][j]
        return dyna(0,0)