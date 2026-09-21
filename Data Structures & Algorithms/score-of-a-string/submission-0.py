class Solution:
    def scoreOfString(self, s: str) -> int:
        i=0
        sum=0
        for j in range(1,len(s)):
            sum+=abs(ord(s[j])-ord(s[i]))
            i=j
        return sum