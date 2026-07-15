class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=0
        zf=0
        zcount=0
        a=[0]*(len(nums))
        for i in nums:
            if i==0:
                zf=1
                zcount+=1
            else:
                if prod==0:
                    prod=1
                prod=prod*i
        if zcount>1:
            return a
        for i in range(len(nums)):
            if zf==0 :
                a[i]=int(prod/nums[i])
            elif zf==1 and nums[i]!=0:
                continue
            elif zf==1 and nums[i]==0:
                a[i]=int(prod)
        return a

