class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rep={}
        for i in strs:
            j=''.join(sorted(i))
            if j in rep:
                rep[j].append(i)
            else:
                rep[j]=[i]
        return list(rep.values())
        