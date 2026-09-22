class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=[]
        j=0
        minvalue=float("inf")
        for i in strs:
            if len(i)<minvalue:
                minvalue=len(i)
        for j in range(minvalue):
            for i in range(len(strs)-1):
                if strs[i][j]!=strs[i+1][j]:
                    return "".join(ans)
            ans.append(strs[0][j])
        return "".join(ans)
            
