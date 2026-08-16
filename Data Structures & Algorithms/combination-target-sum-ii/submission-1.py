class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        def comb(i,amt,curr):
            if amt==0:
                ans.append(curr[:])
                return
            if amt<0:
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if candidates[j]>amt:
                    break
                curr.append(candidates[j])
                comb(j+1,amt-candidates[j],curr)
                curr.pop()
        comb(0,target,[])
        return ans