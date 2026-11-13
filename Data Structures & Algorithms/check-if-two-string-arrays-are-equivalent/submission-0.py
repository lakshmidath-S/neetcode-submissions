class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a1=[]
        a2=[]
        for i in word1:
            for j in i:
                a1.append(j)
        for i in word2:
            for j in i:
                a2.append(j)
        return a1==a2
        
