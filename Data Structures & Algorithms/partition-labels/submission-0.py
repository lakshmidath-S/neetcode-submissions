class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={}
        for i in range(len(s)):
            last[s[i]]=i
        ans=[]
        l=0
        i=0
        while i<len(s):
            a=s[i]
            l=max(l,last[a])
            j=i
            while j<=l:
                l=max(l,last[s[j]])
                j+=1
            ans.append(s[i:j])
            i=j
        return [len(i) for i in ans ]

