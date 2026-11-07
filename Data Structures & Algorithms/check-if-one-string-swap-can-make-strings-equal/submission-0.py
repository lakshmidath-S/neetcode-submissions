class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        points=[]
        for i in range(len(s2)):
            if s1[i]!=s2[i]:
                points.append(i)
        if len(points)==0:
            return True
        if len(points)!=2:
            return False
        i,j=points
        return s1[i]==s2[j] and s1[j]==s2[i]