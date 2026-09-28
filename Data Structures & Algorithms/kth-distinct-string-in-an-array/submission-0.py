class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq={}
        set2=[]
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i,j in freq.items():
            if j==1:
                set2.append(i)
        if len(set2)<k:
            return ""
        return set2[k-1]