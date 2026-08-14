class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        maxlen=1
        start=0
        for i in range(n):
            dp[i][i]=True
        for length in range(2,n+1):
            for i in range(n-length+1):
                j=i+length-1
                if s[i]==s[j] and (dp[i+1][j-1] or length==2):
                    dp[i][j]=True
                    if length>maxlen:
                        start=i
                        maxlen=length
        return s[start:start+maxlen]
    