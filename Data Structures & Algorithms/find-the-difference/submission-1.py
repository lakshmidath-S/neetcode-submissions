from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq1=Counter(s)
        freq2=Counter(t)
        for i,j in freq2.items():
            if i in freq2 and i not in freq1:
                return i
            elif freq1[i]!=freq2[i]:
                return i
            