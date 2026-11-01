class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans=[]
        while columnNumber>0:
            columnNumber-=1
            a=columnNumber%26
            columnNumber//=26
            ans.append(chr(65+a))
        return "".join(ans[::-1])
