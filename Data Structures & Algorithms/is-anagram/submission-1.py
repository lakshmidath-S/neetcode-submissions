class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        freq={}
        for x in s:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
        for x in t:
            if x in freq:
                freq[x]-=1
            else:
                return False
        for x in freq:
            if freq[x]>0 or freq[x]>0:
                return False
        return True
        