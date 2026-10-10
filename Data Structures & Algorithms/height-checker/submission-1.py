class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        freq=[0]*101
        for h in heights:
            freq[h]+=1
        count=0
        ex_height=1
        for h in heights:
            while freq[ex_height]==0:
                ex_height+=1
            if h!=ex_height:
                count+=1
            freq[ex_height]-=1
        return count