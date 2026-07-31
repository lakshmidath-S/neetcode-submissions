# BETTER VERSION
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r,l=0,0
        n=len(s)
        freq={}
        maxlen=0
        maxfreq=0
        while r<n:
            freq[s[r]]=freq.get(s[r],0)+1
            maxfreq=max(maxfreq,freq[s[r]])
            while (r-l+1)-maxfreq>k:#invalid
                freq[s[l]]-=1
                l+=1
            #valid
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
