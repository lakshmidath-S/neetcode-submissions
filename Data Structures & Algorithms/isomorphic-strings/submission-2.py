class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map1={}
        map2={}
        for i in range(len(s)):
            a=s[i]
            b=t[i]
            if a in map1 and map1[a]!=b:
                return False
            if b in map2 and map2[b]!=a:
                return False
            map1[a]=b
            map2[b]=a
        return True


