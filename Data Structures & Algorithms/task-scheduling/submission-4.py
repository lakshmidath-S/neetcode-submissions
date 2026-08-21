class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq={}
        for i in tasks:
            freq[i]=freq.get(i,0)+1
        maxfreq=max(freq.values())
        countmax=0
        for f in freq.values():
            if f==maxfreq:
                countmax+=1
        intervels=(n+1)*(maxfreq-1)+countmax
        return max(intervels,len(tasks))

    