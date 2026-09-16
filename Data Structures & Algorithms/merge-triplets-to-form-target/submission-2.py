class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a=[[] for _ in range(3)]
        
        for i in range(len(triplets)):
            x=triplets[i]
            for j in range(3):
                if x[j]==target[j]:
                    if x[0]<=target[0] and x[1]<=target[1] and x[2]<=target[2]:
                        a[j].append(x)
        m1=0
        m2=0
        m3=0
        for i in range(3):
            for j in (a[i]):
                m1=max(m1,j[0])
                m2=max(m2,j[1])
                m3=max(m3,j[2])
        
        return [m1,m2,m3]==target

