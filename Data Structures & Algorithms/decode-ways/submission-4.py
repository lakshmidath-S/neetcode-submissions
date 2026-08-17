class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        next1=1
        next2=0
        for i in range(n-1,-1,-1):
            curr=0
            if s[i]!='0':
                curr=next1
                if i+1<n and 9<int(s[i:i+2])<27:
                    curr+=next2
            next2=next1
            next1=curr
        return next1