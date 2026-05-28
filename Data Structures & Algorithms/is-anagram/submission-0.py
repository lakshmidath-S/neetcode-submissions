class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1={}
        freq2={}
        for x in s:
            if x in freq1:
                freq1[x]+=1
            else:
                freq1[x]=1
        for x in t:
            if x in freq2:
                freq2[x]+=1
            else:
                freq2[x]=1
        return freq1==freq2