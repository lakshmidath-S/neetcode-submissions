class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0
        j=0
        n=len(s)
        m=len(t)
        while i<n and j<m:
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                i+=1
        if j==m:
            return 0
        else:
            return m+n-i-j