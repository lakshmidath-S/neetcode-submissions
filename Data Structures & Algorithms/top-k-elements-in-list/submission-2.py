class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        listtt=[]
        for i in range(k):
            a=max(freq,key=freq.get)
            listtt.append(a)
            del(freq[a])
        return listtt