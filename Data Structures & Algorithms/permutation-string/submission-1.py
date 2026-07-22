class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freq={}
        for i in range(len(s1)):
            if s1[i] not in freq:
                freq[s1[i]]=1
            else:
                freq[s1[i]]+=1
        freq2={}
        k=len(s1)
        for i in range(len(s1)):
            if s2[i] not in freq2:
                freq2[s2[i]]=1
            else:
                freq2[s2[i]]+=1
        if freq==freq2:
            return True
        else:
            i=0
            while(k<len(s2)):
                a=i
                i+=1
                
                if s2[k] not in freq2:
                    freq2[s2[k]]=1
                else:
                    freq2[s2[k]]+=1
                if freq2[s2[a]]>1:
                    freq2[s2[a]]-=1
                elif freq2[s2[a]]==1:
                    del freq2[s2[a]]
                if freq==freq2:
                    return True
                k+=1
        return False
            