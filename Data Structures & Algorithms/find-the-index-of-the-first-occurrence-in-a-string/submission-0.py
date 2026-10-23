class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans=-1
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j]!=needle[j]:
                    break
            if j==len(needle)-1 and haystack[i + j] == needle[j]:
                ans=i
                break
        return ans