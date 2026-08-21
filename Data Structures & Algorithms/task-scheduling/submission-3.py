class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        freq={}
        for i in tasks:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        key = max(freq, key=freq.get)
        a=freq[key]
        count=(n+1)*(a-1)
        while freq and  max(freq.values())==a:
            count+=1
            key = max(freq, key=freq.get)
            a=freq[key]
            del freq[key]

        #update count ( count+=1 ) if same another element of same freq is found
        return max(count,len(tasks))