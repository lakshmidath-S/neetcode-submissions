class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        m1=m2=m3=0
        for x,y,z in (triplets):
            if x<=target[0] and y<=target[1] and z<=target[2]:
                m1=max(m1,x)
                m2=max(m2,y)
                m3=max(m3,z)
        
        return [m1,m2,m3]==target

