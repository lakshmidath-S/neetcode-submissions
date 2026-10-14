class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i=0
        n=len(blocks)
        black=0
        while(i<k):
            if blocks[i]=='B':
                black+=1
            i+=1
        maxcount=black
        while i<n:
            if blocks[i-k]=='W' and blocks[i]=='B':
                black+=1
            elif blocks[i-k]=='B' and blocks[i]=='W':
                black-=1
            i+=1
            maxcount=max(maxcount,black)
        return k-maxcount
            
