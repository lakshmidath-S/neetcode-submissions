class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        freqt={}
        for i in t:
            if i in freqt:
                freqt[i]+=1
            else:
                freqt[i]=1
        n1=len(s)
        n2=len(t)
        window={}
        i=0
        j=0
        need=len(freqt)
        have=0
        a=""
        lenmin=float('inf')
        while j<n1:
            if s[j] in window:
                window[s[j]]+=1
            else:
                window[s[j]]=1
            if s[j] in freqt and window[s[j]]==freqt[s[j]]:
                have+=1
            while have==need:
                if lenmin>j-i+1:
                    lenmin=j-i+1
                    a=s[i:j+1]
                if s[i] in window:
                    window[s[i]]-=1
                if s[i] in freqt and window[s[i]]<freqt[s[i]]:
                    have-=1
                i+=1
            j+=1
        return a
            
                    
