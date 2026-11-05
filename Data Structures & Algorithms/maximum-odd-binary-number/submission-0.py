class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones=0
        for i in range(len(s)):
            if s[i]=='1':
                ones+=1
        zeros=len(s)-ones
        return '1'*(ones-1)+'0'*zeros+'1'

