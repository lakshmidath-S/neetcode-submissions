class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=len(s)
        j=0
        i=n-1
        maxlen=0
        while i>-1:
            if s[i]==' ':
                i-=1
                continue
            j=i
            while s[j]!=' ' and j>-1:
                j-=1
            return i-j
        return i

            