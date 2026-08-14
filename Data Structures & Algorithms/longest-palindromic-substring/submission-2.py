class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen=0
        maxstring=''
        for i in range(len(s)):
            left=i
            right=i
            left2=i
            right2=i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                if right-left-1>maxlen:
                    maxstring=s[left+1:right]
                    maxlen=right-left-1
            left=i
            right=i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                if right-left-1>maxlen:
                    maxstring=s[left+1:right]
                    maxlen=right-left-1
        return maxstring
            
            
            
