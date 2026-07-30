class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        if nums[j]>=nums[i]: #sorted array
            return nums[i]
        mid=0
        while i<=j:
            mid=(i+j)//2
            if mid==0:
                if nums[mid+1]>nums[mid]:
                    return nums[mid]
                else :
                    return nums[mid+1]
            if mid==len(nums)-1:
                if nums[mid-1]>nums[mid]:
                    return nums[mid]
                else :
                    return nums[mid-1]
            if (nums[mid-1]>nums[mid] and nums[mid+1]>nums[mid]):
                return nums[mid]
            if nums[mid]>nums[j]:
                i=mid+1
                continue
            else:
                j=mid
                continue
        return nums[mid]
