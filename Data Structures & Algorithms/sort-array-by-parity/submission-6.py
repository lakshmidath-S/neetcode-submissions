class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i=0
        n=len(nums)
        j=n-1
        while i<j:
            while i<j and nums[i]%2==0:
                i+=1
            while i<j and nums[j]%2==1:
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
            if i<j:
                i+=1
                j-=1
        return nums