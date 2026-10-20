class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        j=0
        n=len(nums)
        while j<n:
            if nums[j]>=0:
                break
            j+=1
        i=j-1
        soted=[]
        while i>-1 and j<n:
            if abs(nums[i])>abs(nums[j]):
                soted.append(nums[j]**2)
                j+=1
            elif abs(nums[i])<=abs(nums[j]):
                soted.append(nums[i]**2) 
                i-=1
        while i>-1:
            soted.append(nums[i]**2) 
            i-=1
        while j<n:
            soted.append(nums[j]**2)
            j+=1
        return soted

