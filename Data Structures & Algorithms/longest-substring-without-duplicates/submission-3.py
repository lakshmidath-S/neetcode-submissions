class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        maxlen=0
        seen=set()
        for k in range(len(s)):
            while s[k] in seen:
                seen.remove(s[i])
                i+=1
            else:
                seen.add(s[k])
                leng=k-i+1
                maxlen=max(leng,maxlen)
        return maxlen