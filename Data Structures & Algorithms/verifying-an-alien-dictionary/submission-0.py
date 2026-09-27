class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank={}
        for i in range(len(order)):
            rank[order[i]]=i
        for i in range(0,len(words)-1):
            a=words[i]
            b=words[i+1]
            j=0
            while j<len(a) and j<len(b):
                if a[j]!=b[j]:
                    if rank[a[j]]>rank[b[j]]:
                        return False
                    break
                j+=1
            if j==len(b) and j<len(a):
                return False

        return True