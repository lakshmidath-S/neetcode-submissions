class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted={}
        for a,b in trust:
            trusted[b]=trusted.get(b,0)+1
        if trusted[b]>=n-1:
            return b
        else :
            return -1
