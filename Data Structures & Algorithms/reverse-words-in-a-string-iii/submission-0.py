class Solution:
    def reverseWords(self, s: str) -> str:
        ans=[]
        i=0
        j=0
        while j<(len(s)):
            if s[j]==' ':
                ans.append(s[i:j][::-1])
                ans.append(" ")
                i=j+1
            j+=1
        ans.append(s[i:j][::-1])
        return "".join(ans)

