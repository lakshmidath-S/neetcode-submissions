class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(nums)
        def  back(amt,i,curr):
            if amt==0:
                ans.append(curr[:])
                return
            if i>=n or amt<0:
                return
            curr.append(nums[i])
            back(amt-nums[i],i,curr)
            curr.pop()
            back(amt,i+1,curr)
        back(target,0,[])
        return ans
