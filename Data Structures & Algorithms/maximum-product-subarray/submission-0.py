class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmax=nums[0]
        cmin=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            x=nums[i]
            if x<0:
                cmax,cmin=cmin,cmax
            cmax=max(x,cmax*x)
            cmin=min(x,cmin*x)
            ans=max(cmax,ans)
        return ans

            

        