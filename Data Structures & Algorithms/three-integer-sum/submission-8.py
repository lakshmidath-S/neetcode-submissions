class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=len(nums)
        if l<3:
            return []
        nums.sort()
        if nums[0]>0:
                return []
        ans=set()
        for i in range(l-2):
            k=l-1
            j=i+1
            while(j<k):
                if nums[j]+nums[k]==0-nums[i]:
                    ans.add(tuple([nums[i],nums[j],nums[k]]))
                elif nums[j]+nums[k]<0-nums[i]:
                    k+=1
                else :
                    j-=1
                k-=1
                j+=1
        return[list(t) for t in ans]