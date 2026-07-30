class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j=0,len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                return mid
            if nums[i]<=nums[mid]:
                if nums[mid]>target>=nums[i]:
                    j=mid-1
                else:
                    i=mid+1
            elif nums[j]>nums[mid]:
                if nums[mid]<target<=nums[j]:
                    i=mid+1
                else:
                    j=mid-1
        return -1