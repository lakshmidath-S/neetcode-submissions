from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        freq=Counter(s)
        maxvalue=max(x for x in freq.values() if x%2==1)
        minvalue=min(x for x in freq.values() if x%2==0)
        return maxvalue-minvalue