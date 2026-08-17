class Solution:
    def numDecodings(self, s: str) -> int:
        dp={}
        def back(i):
            ans=0
            if i==len(s):
                return 1
            if s[i]=='0':
                return 0
            if i in dp:
                return dp[i]
            ans=back(i+1)
            if i+1<len(s) and 9<int(s[i:i+2])<27:
                ans+=back(i+2)
            dp[i]=ans
            return ans
        return back(0)
            
            