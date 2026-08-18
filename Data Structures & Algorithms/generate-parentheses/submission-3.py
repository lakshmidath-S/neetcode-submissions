class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp=[[""]]+[[]for _ in range(n)]
        for j in range(1,n+1):
            for i in range(j):
                for left in dp[i]:
                    for right in dp[j-i-1]:
                        dp[j].append("(" + left + ")" + right)
        return dp[n]