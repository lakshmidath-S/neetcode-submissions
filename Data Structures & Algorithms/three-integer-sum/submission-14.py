class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=len(nums)
        nums.sort()
        ans=[]
        for i in range(l-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            curr=0-nums[i]
            k=l-1
            j=i+1
            while(j<k):
                target=nums[j]+nums[k]
                if target==curr:
                    ans.append([nums[i],nums[j],nums[k]])
                    while j+1<k and nums[j]==nums[j+1] :
                        j+=1
                    while j<k and nums[k]==nums[k-1] :
                        k-=1
                elif target<curr:
                    k+=1
                else :
                    j-=1
                k-=1
                j+=1
        return ans